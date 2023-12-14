from typing import Iterator
import pytest
from pymongo.database import Database


def prune_database(database: Database) -> None:
    collections = database.list_collection_names()

    for collection in collections:
        database.drop_collection(collection)  # to delete the collection
        # database[collection].delete_many({}) # to erase all documents


@pytest.fixture
def database() -> Iterator[Database]:
    from app_pymongo.database import database

    prune_database(database)

    yield database

    prune_database(database)
