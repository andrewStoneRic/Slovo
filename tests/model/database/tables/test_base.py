from src.model.database.tables.base import Base

def test_create_Base():
    base = Base()
    
    assert isinstance(base, Base)
    