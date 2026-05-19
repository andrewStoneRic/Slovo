from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
# TYPE_CHECKING для того, чтобы IDE видела WordBase, 
# но Python не создавал рекурсивного импорта
if TYPE_CHECKING: 
    from .words import WordBase
    from .chunks import ChunkBase
    from .contexts import ContextBase

class LanguageBase(Base):
    """Таблица языков"""
    
    __tablename__ = "languages"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    code: Mapped[str] = mapped_column(String(5))
    words: Mapped[list[WordBase]] = relationship(back_populates="language")
    chunks: Mapped[list[ChunkBase]] = relationship(back_populates="language")
    contexts: Mapped[list[ContextBase]] = relationship(back_populates="language")