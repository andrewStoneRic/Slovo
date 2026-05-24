from src.model.database.managers.baseManager import BaseManager
from src.model.database.tables.words import WordBase

def test_create_and_init_BaseManager(session):
    baseManager = BaseManager(
        session=session,
        table=WordBase
    )

    # Create
    assert isinstance(baseManager, BaseManager)

    # Init
    assert baseManager.session == session
    assert baseManager.table == WordBase

def test_add_some_obj_in_db(session):
    baseManager = BaseManager(
        session=session,
        table=WordBase
    )

    word = baseManager.add(
        text="hello",
        langID=0,
        metaWords={},
    )

    assert word in session
    assert session.query(WordBase).filter_by(text="hello").one() 

def test_get_all_data_in_db(session):

    baseManager = BaseManager(
        session=session,
        table=WordBase
    )

    word0 = baseManager.add(
        text="hello",
        langID=0,
        metaWords={},
    )

    word1 = baseManager.add(
        text="hi",
        langID=0,
        metaWords={},
    )

    assert baseManager.get_all() == [word0, word1]

