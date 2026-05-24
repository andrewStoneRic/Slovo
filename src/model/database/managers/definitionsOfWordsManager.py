from .baseManager import BaseManager
from ..tables.definitionsOfWords import DefinitionsOfWordBase

class DefinitionsOfWordsManager(BaseManager):
    """Менаджер определений слов"""

    def __init__(self, session):
        super().__init__(session, DefinitionsOfWordBase)
