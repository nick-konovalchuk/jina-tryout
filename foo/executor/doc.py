from docarray import BaseDoc

__all__ = ["Text", "FooDoc"]


class Text(BaseDoc):
    text: str


class FooDoc(Text):
    foo: str
