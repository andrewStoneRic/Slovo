from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .wordPartOfSpeech import wordPartOfSpeech
if TYPE_CHECKING: 
    from .words import WordBase

class PartOfSpeechBase(Base): 
    __tablename__ = "partsOfSpeech"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    
    words: Mapped[list["WordBase"]] = relationship(
        secondary=wordPartOfSpeech, back_populates="partsOfSpeech"
    )