from src.model.appModel import AppModel

def test_create_and_init_appModel():
    
    model = AppModel()
    
    assert isinstance(model, AppModel)