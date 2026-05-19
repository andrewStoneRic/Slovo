from src.model.database.tables.base import Base
from src.model.database.tables.languages import LanguageBase

def test_create_and_init_LanguageBase():
    russian = LanguageBase(
        name="Russian",
        code="ru"
    )
    
    # Create
    assert isinstance(russian, LanguageBase)
    assert issubclass(LanguageBase, Base)
    
    # Init
    assert russian.name == "Russian"
    assert russian.code == "ru"
    assert russian.words == []
    assert russian.chunks == []
    assert russian.contexts == []