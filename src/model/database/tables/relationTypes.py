from typing import TYPE_CHECKING 

from sqlalchemy import Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .wordWordRelation import wordWordRelation
if TYPE_CHECKING:
    from .words import WordBase

class RelationTypeBase(Base):
    """Таблица с типами связи между словами"""
    
    __tablename__ = "relationTypes"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    isDerectional: Mapped[bool] = mapped_column(Boolean())
