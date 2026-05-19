from sqlalchemy import Table

from src.model.database.tables.wordChunk import wordChunk

def test_create_and_init_wordChunk():
    
    # Create
    assert isinstance(wordChunk, Table)
    
    # Init
    columns = [col.name for col in wordChunk.columns]
    
    assert "wordID" in columns
    assert "chunkID" in columns
    assert "positionInChunk" in columns
    
    assert len(columns) == 3