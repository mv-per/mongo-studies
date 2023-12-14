import pytest
from mongoengine.connection import get_db


@pytest.fixture()
def database():
    from database import connection, DATABASE_NAME

    connection.drop_database(DATABASE_NAME)

    return get_db()
