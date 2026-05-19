from typing import TYPE_CHECKING, Any

from sqlalchemy import JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
if TYPE_CHECKING: 
    from .languages import LanguageBase
    from .wordContext import WordContext
    from .chunkContext import ChunkContextBase

class ContextBase(Base): 
    __tablename__ = "contexts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    langID: Mapped[int] = mapped_column(ForeignKey("languages.id"))
    language: Mapped[LanguageBase] = relationship(back_populates="contexts")
    words: Mapped[list[WordContext]] = relationship(
        back_populates="context", cascade="all, delete-orphan"
    )
    chunks: Mapped[list[ChunkContextBase]] = relationship(
        back_populates="context", cascade="all, delete-orphan"
    )
    metaContext: Mapped[dict[str: Any]] = mapped_column(JSON)