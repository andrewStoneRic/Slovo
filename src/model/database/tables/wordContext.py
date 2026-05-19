from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
if TYPE_CHECKING:
    from .words import WordBase
    from .contexts import ContextBase

class WordContext(Base): 
    __tablename__ = "wordContext"
    
    wordID: Mapped[int] = mapped_column(ForeignKey("words.id"), primary_key=True)
    contextID: Mapped[int] = mapped_column(ForeignKey("contexts.id"), primary_key=True)
    positionInContext: Mapped[int] = mapped_column(Integer())
    
    word: Mapped[WordBase] = relationship(
        back_populates="contexts"
    )
    context: Mapped[ContextBase] = relationship(
        back_populates="words"
    )