from src.model.database.tables.base import Base
from src.model.database.tables.definitionsOfWords import DefinitionsOfWordBase

def test_create_and_init_DefinitionsOfWordBase():
    definition_of_hello = DefinitionsOfWordBase(
        wordID=0,
        text="Greating",
        priority=1
    )
    
    # Create
    assert isinstance(definition_of_hello, DefinitionsOfWordBase)
    assert issubclass(DefinitionsOfWordBase, Base)
    
    # Init
    assert definition_of_hello.wordID == 0
    assert definition_of_hello.text == "Greating"
    assert definition_of_hello.priority == 1