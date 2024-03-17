from docarray import DocList
from jina import Executor, requests

from .doc import FooDoc, BarDoc

__all__ = ["Bar"]


class Bar(Executor):
    @requests
    def bar(self, docs: DocList[FooDoc], **kwargs) -> DocList[BarDoc]:
        docs = DocList([BarDoc(**doc.dict(), bar="bar") for doc in docs])
        return docs
