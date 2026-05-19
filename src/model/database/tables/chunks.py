from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .languages import LanguageBase
    from .chunkContext import ChunkContextBase

class ChunkBase(Base):
    __tablename__ = "chunks"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    langID: Mapped[int] = mapped_column(ForeignKey("languages.id"))
    language: Mapped[LanguageBase] = relationship(back_populates="chunks")
    contexts: Mapped[list[ChunkContextBase]] = relationship(
        back_populates="chunk", cascade="all, delete-orphan"
    )