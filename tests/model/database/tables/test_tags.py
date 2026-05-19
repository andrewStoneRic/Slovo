import pytest

from src.exceptions.hashTagNotFoundError import HashTagNotFoundError

from src.model.database.tables.base import Base
from src.model.database.tables.tags import TagBase

def test_create_and_init_TagBase():
    tag = TagBase(
        name="#new"
    )
    
    # Create
    assert isinstance(tag, TagBase)
    assert issubclass(TagBase, Base)
    
    # Init
    assert tag.name == "#new"
    assert tag.words == []
    
def test_validate_name_raises_error_when_name_without_hash():
    with pytest.raises(HashTagNotFoundError):
        tag = TagBase(
            name="new"
        )
    
    