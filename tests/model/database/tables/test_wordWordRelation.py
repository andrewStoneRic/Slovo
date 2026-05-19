from sqlalchemy import Table

from src.model.database.tables.wordWordRelation import wordWordRelation

def test_create_and_init_wordWordRelation():
    
    # Create
    assert isinstance(wordWordRelation, Table)
    
    # Init
    columns = [col.name for col in wordWordRelation.columns]
    
    assert "firstWordID" in columns
    assert "secondWordID" in columns
    assert "relationTypeID" in columns
    
    assert len(columns) == 3