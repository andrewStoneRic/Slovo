from src.model.database.tables.base import Base
from src.model.database.tables.contexts import ContextBase

def test_create_and_init_ContextBase():
    context = ContextBase(
        text = "Hello World, my friend",
        langID=0,
        metaContext={},
    )
    
    # Create
    assert isinstance(context, ContextBase)
    assert issubclass(ContextBase, Base)
    
    # Init
    assert context.text == "Hello World, my friend"
    assert context.langID == 0
    assert context.language == None
    assert context.words == []
    assert context.chunks == []
    assert context.metaContext == {}