from src.model.database.managers.baseManager import BaseManager
from src.model.database.managers.wordsManager import WordsManager
from src.model.database.tables.words import WordBase

def test_create_and_init_WordsManager(session):
    wordsManager = WordsManager(
        session=session,
    )

    # Create
    assert isinstance(wordsManager, WordsManager)
    assert issubclass(WordsManager, BaseManager)

    # Init 
    assert wordsManager.session == session
    assert wordsManager.table == WordBase
