import cattrs
from pytest_regressions.data_regression import DataRegressionFixture
from pymongo.database import Database
from app_pymongo.models.user import User


def test_create_user(database: Database, data_regression: DataRegressionFixture):
    user = User(name="John", email="Jhon@email.com", password="passkey")

    serialized_user = cattrs.unstructure(user)

    database.users.insert_one(serialized_user)

    users_count = database.users.count_documents({})
    users = database.users.find({})

    assert users_count == 1
    stored_user = users[0]
    stored_user.pop("_id")

    data_regression.check(stored_user)


def test_edit_user(database: Database, data_regression: DataRegressionFixture):
    user = User(name="John", email="Jhon@email.com", password="passkey")

    serialized_user = cattrs.unstructure(user)

    database.users.insert_one(serialized_user)

    users_count = database.users.count_documents({})
    assert users_count == 1

    database.users.update_one({"email": "Jhon@email.com"}, {"$set": {"name": "Mary"}})

    user = database.users.find_one({"email": "Jhon@email.com"})

    assert users_count == 1

    user.pop("_id")

    data_regression.check(user)


def test_create_many_user(database: Database, data_regression: DataRegressionFixture):
    users = [
        User(name="John", email="Jhon@email.com", password="passkey"),
        User(name="John3", email="Jhon3@email.com", password="passkey"),
        User(name="John2", email="Jhon2@email.com", password="passkey"),
        User(name="John1", email="Jhon1@email.com", password="passkey"),
    ]

    serialized_users = [cattrs.unstructure(user) for user in users]

    database.users.insert_many(serialized_users)

    users_count = database.users.count_documents({})
    stored_users = database.users.find({})

    assert users_count == len(users)

    data = {}
    for i, stored_user in enumerate(stored_users):
        stored_user.pop("_id")
        data[i] = stored_user

    data_regression.check({"data": data})


def test_delete_many(database: Database):
    users = [
        User(name="John", email="Jhon@email.com", password="passkey"),
        User(name="John", email="Jhon3@email.com", password="passkey"),
        User(name="Fred", email="Jhon2@email.com", password="passkey"),
        User(name="Mary", email="Jhon1@email.com", password="passkey"),
    ]

    serialized_users = [cattrs.unstructure(user) for user in users]

    database.users.insert_many(serialized_users)

    users_count = database.users.count_documents({})
    assert users_count == len(users)

    database.users.delete_many({"name": "John"})

    users_count = database.users.count_documents({})
    assert users_count == 2
