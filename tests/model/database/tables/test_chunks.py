from src.model.database.tables.base import Base
from src.model.database.tables.chunks import ChunkBase

def test_create_and_init_ChunkBase():
    chunk = ChunkBase(
        text="Hello World",
        langID=0
    )
    
    # Create
    assert isinstance(chunk, ChunkBase)
    assert issubclass(ChunkBase, Base)
    
    # Init
    assert chunk.text == "Hello World"
    assert chunk.langID == 0
    assert chunk.language == None
    assert chunk.contexts == []
    