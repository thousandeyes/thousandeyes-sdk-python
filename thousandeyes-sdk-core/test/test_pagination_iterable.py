from types import SimpleNamespace

from thousandeyes_sdk.core.pagination_iterable import PaginationIterable


def test_iterable_uses_cursor_from_next_href():
    calls = []

    def method(**params):
        calls.append(params.copy())
        if params.get("cursor") is None:
            links = SimpleNamespace(next="https://example.com/items?cursor=abc")
            items = ["first", "second"]
        else:
            links = SimpleNamespace(next=None)
            items = ["third"]
        return SimpleNamespace(links=links, items=items)

    responses = list(PaginationIterable(method, lambda response: response.items))

    assert responses == ["first", "second", "third"]
    assert calls == [{}, {"cursor": "abc"}]


def test_iterable_reads_cursor_from_links_mapping():
    calls = []

    def method(**params):
        calls.append(params.copy())
        if params.get("pageCursor") is None:
            links = {"next": {"href": "https://example.com?foo=1&pageCursor=xyz"}}
            items = ["alpha"]
        else:
            links = {"next": None}
            items = ["beta"]
        return SimpleNamespace(links=links, items=items)

    responses = list(PaginationIterable(method, lambda response: response.items, cursor_param="pageCursor"))

    assert responses == ["alpha", "beta"]
    assert calls == [{}, {"pageCursor": "xyz"}]


def test_iterable_stops_when_no_cursor_param_present():
    calls = []

    def method(**params):
        calls.append(params.copy())
        if params.get("cursor") is None:
            links = {"next": "/next/page"}
            items = ["one"]
        else:
            links = {"next": None}
            items = ["two"]
        return SimpleNamespace(links=links, items=items)

    responses = list(PaginationIterable(method, lambda response: response.items))

    assert responses == ["one"]
    assert calls == [{}]


def test_iterable_stops_on_repeated_cursor():
    calls = []

    def method(**params):
        calls.append(params.copy())
        links = {"next": "https://example.com?cursor=same"}
        return SimpleNamespace(links=links, items=["only"])

    responses = list(PaginationIterable(method, lambda response: response.items, cursor="same"))

    assert responses == ["only"]
    assert calls == [{"cursor": "same"}]
