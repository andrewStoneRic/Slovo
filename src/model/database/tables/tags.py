from typing import TYPE_CHECKING

from sqlalchemy.orm import (Mapped, mapped_column, 
                            relationship, validates)

from ....exceptions.hashTagNotFoundError import HashTagNotFoundError

from .base import Base
from .wordTag import wordTag
if TYPE_CHECKING:
    from .words import WordBase

class TagBase(Base): 
    """Таблица тэгов"""
    
    __tablename__ = "tags"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    words: Mapped[list["WordBase"]] = relationship(
        secondary=wordTag, back_populates="tags"
    )
    
    @validates('name')
    def validate_name(self, key: str, name: str):
        """Проверяет есть ли # перед названием тэга"""
        
        if not name.startswith('#'):
            raise HashTagNotFoundError("Не найден # перед именем тэга")
        
        return name
        
    