from docarray import BaseDoc

__all__ = ["FooDoc", "BarDoc"]


class FooDoc(BaseDoc):
    text: str
    foo: str


class BarDoc(FooDoc):
    bar: str
