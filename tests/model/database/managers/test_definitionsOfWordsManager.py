from src.model.database.managers.baseManager import BaseManager
from src.model.database.managers.definitionsOfWordsManager import DefinitionsOfWordsManager
from src.model.database.tables.definitionsOfWords import DefinitionsOfWordBase

def test_create_and_init_DefinitionsOfWordsManager(session):
    definitionsOfWordsManager = DefinitionsOfWordsManager(
        session=session,
    )

    # Create
    assert isinstance(definitionsOfWordsManager, DefinitionsOfWordsManager)
    assert issubclass(DefinitionsOfWordsManager, BaseManager)

    # Init 
    assert definitionsOfWordsManager.session == session
    assert definitionsOfWordsManager.table == DefinitionsOfWordBase
