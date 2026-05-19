from src.model.database.tables.base import Base
from src.model.database.tables.chunkContext import ChunkContextBase

def test_create_and_init_ChunkContextBase():
    chunkContext = ChunkContextBase(
        chunkID=0,
        contextID=0,
        startOffset=2,
        endOffset=5
    )
    
    # Create
    assert isinstance(chunkContext, ChunkContextBase)
    assert issubclass(ChunkContextBase, Base)
    
    # Init
    assert chunkContext.chunkID == 0
    assert chunkContext.contextID == 0
    assert chunkContext.startOffset == 2
    assert chunkContext.endOffset == 5
    assert chunkContext.chunk == None
    assert chunkContext.context == None