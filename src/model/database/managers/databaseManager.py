from sqlalchemy.orm import Session

class DatabaseManager:
    """Менеджер базы данных"""

    def __init__(self, session: Session):
        self.session = session
    
    def make_a_word(self):
       pass 
