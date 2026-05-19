from src.model.database.tables.base import Base
from src.model.database.tables.relationTypes import RelationTypeBase

def test_create_and_init_RelationTypeBase():
    my_type = RelationTypeBase(
        name="synonims",
        isDerectional=True
    )
    
    # Create 
    assert isinstance(my_type, RelationTypeBase)
    assert issubclass(RelationTypeBase, Base)
    
    # Init
    assert my_type.name == "synonims"
    assert my_type.isDerectional == True