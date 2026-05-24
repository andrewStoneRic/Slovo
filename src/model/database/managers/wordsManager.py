from .baseManager import BaseManager
from ..tables.words import WordBase 

class WordsManager(BaseManager):
    """Менаджер слов"""

    def __init__(self, session):
        super().__init__(session, WordBase)

