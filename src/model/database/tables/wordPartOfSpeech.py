from sqlalchemy import Column, Table, ForeignKey

from .base import Base

wordPartOfSpeech = Table(
    "wordPartOfSpeech",
    Base.metadata,
    Column("wordID", ForeignKey("words.id"), primary_key=True),
    Column("partOfSpeechID", ForeignKey("partsOfSpeech.id"), primary_key=True)
)