from src.model.database.tables.base import Base
from src.model.database.tables.wordContext import WordContext

def test_create_and_init_WordChunk():
    wordContext = WordContext(
        wordID=0,
        contextID=0,
        positionInContext=2
    )
    
    # Create
    assert isinstance(wordContext, WordContext)
    assert issubclass(WordContext, Base)
    
    # Init
    
    assert wordContext.wordID == 0
    assert wordContext.contextID == 0
    assert wordContext.positionInContext == 2
    assert wordContext.word == None
    assert wordContext.context == None
