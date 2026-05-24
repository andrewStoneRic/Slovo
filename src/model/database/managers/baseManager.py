from typing import TypeVar, Generic

from sqlalchemy.orm import Session

T = TypeVar('T')

class BaseManager(Generic[T]):
    """Минимальный менеджер"""

    def __init__(self, session: Session, table):
        self.session = session
        self.table = table

    def add(self, **kwargs) -> T: 
        """Добавить объект"""
        obj = self.table(**kwargs)
        self.session.add(obj)
        self.session.commit()
        return obj

    def get_all(self) -> list[T]:
        """Получить все объекты"""

        return self.session.query(self.table).all()

        
