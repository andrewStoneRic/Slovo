from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
if TYPE_CHECKING: 
    from .words import WordBase 


class DefinitionsOfWordBase(Base):
    """Таблица определений слов"""
    
    __tablename__ = "definitionsOfWords"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    wordID: Mapped[int] = mapped_column(ForeignKey("words.id"))
    word: Mapped["WordBase"] = relationship(back_populates="definitions")
    text: Mapped[str]
    priority: Mapped[int] = mapped_column(Integer())