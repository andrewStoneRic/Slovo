
from src.model.database.tables.base import Base
from src.model.database.tables.partsOfSpeech import PartOfSpeechBase

def test_create_and_init_PartOfSpeechBase():
    part = PartOfSpeechBase(
        name="noun"
    )
    
    # Create
    assert isinstance(part, PartOfSpeechBase)
    assert issubclass(PartOfSpeechBase, Base)
    
    # Init
    assert part.name == "noun"
    assert part.words == []