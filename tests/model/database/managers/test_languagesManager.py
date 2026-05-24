from src.model.database.managers.baseManager import BaseManager
from src.model.database.managers.languagesManager import LanguagesManager
from src.model.database.tables.languages import LanguageBase

def test_create_and_init_LanguagesManager(session):
    languagesManager = LanguagesManager(
        session=session,
    )

    # Create
    assert isinstance(languagesManager, LanguagesManager)
    assert issubclass(LanguagesManager, BaseManager)

    # Init 
    assert languagesManager.session == session
    assert languagesManager.table == LanguageBase
