from docarray import DocList
from jina import Executor
from jina import requests

from .doc import BarDoc
from .doc import FooDoc


__all__ = ["Bar"]


class Bar(Executor):
    @requests
    def bar(self, docs: DocList[FooDoc], **kwargs) -> DocList[BarDoc]:
        docs = DocList(
            [BarDoc(id=doc.id, text=doc.text + "bar", foo=doc.foo, bar="bar") for doc in docs]
        )
        return docs
