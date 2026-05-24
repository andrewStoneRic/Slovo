import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.model.database.tables.base import Base

@pytest.fixture(scope="session")
def engine():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    return engine

@pytest.fixture
def session(engine):
    connection = engine.connect()
    transaction = connection.begin()
    SessionLocal = sessionmaker(bind=connection)
    session = SessionLocal()

    yield session

    transaction.rollback()
    session.close()
    connection.close()
