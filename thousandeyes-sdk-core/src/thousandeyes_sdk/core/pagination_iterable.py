# Copyright 2024 Cisco Systems, Inc. and its affiliates
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Callable, Iterable, Iterator
from typing import Any, Mapping, Optional, TypeVar, Generic
from urllib.parse import parse_qs, urlparse

from typing_extensions import ParamSpec

P = ParamSpec("P")
R = TypeVar("R")
I = TypeVar("I")

class PaginationIterable(Generic[P, R, I]):
    """Iterate over cursor-paginated responses.

    Calls ``method`` repeatedly, passing a cursor parameter between calls,
    and yields items obtained from ``items_getter``.
    The next cursor is derived from ``response.data.links`` or ``response.data._links``
    (or mapping equivalents), supporting these link formats:

    - a direct ``href`` string
    - a mapping with a ``href`` key
    - an object with a ``href`` attribute

    Iteration stops when no next cursor is found or the cursor repeats.
    """

    def __init__(
        self,
        method: Callable[P, R],
        items_getter: Callable[[R], Iterable[I]],
        *,
        cursor_param: str = "cursor",
        **params: P.kwargs,
    ) -> None:
        self._method = method
        self._items_getter = items_getter
        self._cursor_param = cursor_param
        self._params: dict[str, Any] = dict(params)

    def __iter__(self) -> Iterator[I]:
        params = dict(self._params)
        last_cursor = params.get(self._cursor_param)

        while True:
            response = self._method(**params)
            items = self._items_getter(response)
            for item in items if items else []:
                yield item

            next_cursor = self._next_cursor_from_response(response)
            if not next_cursor or next_cursor == last_cursor:
                break

            params[self._cursor_param] = next_cursor
            last_cursor = next_cursor

    def _next_cursor_from_response(self, response: Any) -> Optional[str]:
        links = getattr(response, "links", None)

        if links is None:
            links = getattr(response, "_links", None)

        if links is None:
            return None

        next_link = getattr(links, "next", None)
        if next_link is None and isinstance(links, Mapping):
            next_link = links.get("next")

        if next_link is None:
            return None

        if isinstance(next_link, str):
            href = next_link
        elif isinstance(next_link, Mapping):
            href = next_link.get("href")
        else:
            href = getattr(next_link, "href", None)

        if not href:
            return None

        parsed = urlparse(href)
        query_params = parse_qs(parsed.query)
        cursor_values = query_params.get(self._cursor_param)

        if cursor_values:
            return cursor_values[0]
        return None
