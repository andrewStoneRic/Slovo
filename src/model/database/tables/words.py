from typing import TYPE_CHECKING, Any

from sqlalchemy import String, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .wordTag import wordTag
from .wordPartOfSpeech import wordPartOfSpeech
from .wordChunk import wordChunk
if TYPE_CHECKING: 
    from .languages import LanguageBase
    from .definitionsOfWords import DefinitionsOfWordBase
    from .tags import TagBase
    from .partsOfSpeech import PartOfSpeechBase
    from .chunks import ChunkBase
    from .wordContext import WordContext


class WordBase(Base):
    """Таблица слов"""
    
    __tablename__ = "words"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(128), unique=True)
    langID: Mapped[int] = mapped_column(ForeignKey("languages.id"))
    language: Mapped["LanguageBase"] = relationship(back_populates="words")
    
    definitions: Mapped[list[DefinitionsOfWordBase]] = relationship(
        back_populates="word"
    )
        
    tags: Mapped[list[TagBase]] = relationship(
        secondary=wordTag, back_populates="words"
    )
    
    partsOfSpeech: Mapped[list[PartOfSpeechBase]] = relationship(
        secondary=wordPartOfSpeech, back_populates="words"
    )
    
    contexts: Mapped[list[WordContext]] = relationship(
        back_populates="word", cascade="all, delete-orphan"
    )
    
    metaWords: Mapped[dict[str: Any ]] = mapped_column(JSON)
