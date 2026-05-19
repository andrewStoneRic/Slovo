from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
if TYPE_CHECKING:
    from .chunks import ChunkBase
    from .contexts import ContextBase
    
class ChunkContextBase(Base): 
    __tablename__ = "chunkContext"
    
    chunkID: Mapped[int] = mapped_column(ForeignKey("chunks.id"), primary_key=True)
    contextID: Mapped[int] = mapped_column(ForeignKey("contexts.id"), primary_key=True)
    startOffset: Mapped[int] = mapped_column(Integer())
    endOffset: Mapped[int] = mapped_column(Integer())
    
    chunk: Mapped[ChunkBase] = relationship(back_populates="contexts")
    context: Mapped[ContextBase] = relationship(back_populates="chunks")