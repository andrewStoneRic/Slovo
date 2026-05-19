from sqlalchemy import Column, Table, ForeignKey, Integer

from .base import Base

wordChunk = Table(
    "wordChunk",
    Base.metadata,
    Column("wordID", ForeignKey("words.id"), primary_key=True),
    Column("chunkID", ForeignKey("chunks.id"), primary_key=True),
    Column("positionInChunk", Integer)
)