from sqlalchemy import Table

from src.model.database.tables.wordPartOfSpeech import wordPartOfSpeech

def test_create_and_init_wordPartOfSpeeah():
    
    # Create
    assert isinstance(wordPartOfSpeech, Table)
    
    # Init
    columns = [col.name for col in wordPartOfSpeech.columns]
    
    assert "wordID" in columns
    assert "partOfSpeechID" in columns
    
    assert len(columns) == 2