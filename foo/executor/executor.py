from docarray import DocList
from jina import Executor, requests

from .doc import FooDoc, Text

__all__ = ["Foo"]


class Foo(Executor):
    @requests
    def foo(self, docs: DocList[Text], **kwargs) -> DocList[FooDoc]:
        docs = DocList([FooDoc(id=doc.id, text=doc.text + "foo", foo="foo") for doc in docs])
        return docs
