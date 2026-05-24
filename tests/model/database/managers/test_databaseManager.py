from src.model.database.managers.databaseManager import DatabaseManager

def test_create_and_init_databaseManager(session):
    databaseManager = DatabaseManager(
        session=session,
    )
    
    # Create
    assert isinstance(databaseManager, DatabaseManager)

    # Init
    assert databaseManager.session == session

def test_make_a_word(session):
    pass
