from .baseManager import BaseManager
from ..tables.languages import LanguageBase

class LanguagesManager(BaseManager):
    """Менаджер языков"""

    def __init__(self, session):
        super().__init__(session, LanguageBase)
