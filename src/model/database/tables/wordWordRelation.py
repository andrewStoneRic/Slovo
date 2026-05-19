from sqlalchemy import Column, Table, ForeignKey

from .base import Base

wordWordRelation = Table(
    "wordWordRelation",
    Base.metadata,
    Column("firstWordID", ForeignKey("words.id"), primary_key=True),
    Column("secondWordID", ForeignKey("words.id"), primary_key=True),
    Column("relationTypeID", ForeignKey("relationTypes.id"), primary_key=True)
)