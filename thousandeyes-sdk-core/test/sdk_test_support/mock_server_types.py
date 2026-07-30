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

from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass(frozen=True)
class ErrorResponseExpectation:
    status: int
    body: Any
    content_type: str = "application/problem+json"


@dataclass(frozen=True)
class OperationExpectation:
    operation_id: str
    method: str
    path: str
    success_status: int
    success_body: Any = None
    success_content_type: str = "application/json"
    request_body_example: Any = None
    path_param_examples: Dict[str, str] = field(default_factory=dict)
    query_param_examples: Dict[str, str] = field(default_factory=dict)
    error_responses: Dict[str, ErrorResponseExpectation] = field(default_factory=dict)
