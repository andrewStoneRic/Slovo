from sqlalchemy import Column, Table, ForeignKey

from .base import Base

wordTag = Table(
    "wordTag",
    Base.metadata,
    Column("wordID", ForeignKey("words.id"), primary_key=True),
    Column("tagID", ForeignKey("tags.id"), primary_key=True)
)