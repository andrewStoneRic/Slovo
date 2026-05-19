from sqlalchemy import Table

from src.model.database.tables.wordTag import wordTag

def test_create_and_init_wordTag():
    
    # Create
    assert isinstance(wordTag, Table)
    
    # Init
    columns = [col.name for col in wordTag.columns]
    
    assert "wordID" in columns
    assert "tagID" in columns
    
    assert len(columns) == 2