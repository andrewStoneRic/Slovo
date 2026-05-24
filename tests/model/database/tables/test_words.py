from src.model.database.tables.base import Base
from src.model.database.tables.words import WordBase

def test_create_and_init_WordBase():
    word_hello = WordBase(
        text="hello",
        langID=0,
        metaWords={},
    )
    
    # Create
    assert isinstance(word_hello, WordBase)
    assert issubclass(WordBase, Base)
    
    # Init
    assert word_hello.text == "hello"
    assert word_hello.langID == 0
    assert word_hello.language == None
    assert word_hello.definitions == []
    assert word_hello.tags == []
    assert word_hello.partsOfSpeech == []
    assert word_hello.contexts == []
    assert word_hello.metaWords == {}
