from app_mongoengine.models.user import User


def test_crud_user(database) -> None:
    user = User(name="John")

    # create in database
    assert len(database.list_collection_names()) == 0
    count = User.objects().count()
    assert count == 0
    user.save()

    len(database.list_collection_names()) == 1
    count = User.objects().count()
    assert count == 1

    users = [
        User(name="Mary", is_active=True),
        User(name="Sweet", tags=["a", "b"]),
        User(name="Mary", tags=["a", "b"], is_active=False),
        User(name="Mary", is_active=True, tags=["a", "b"]),
    ]
    [User.save(usr) for usr in users]

    # update and save
    count = User.objects(tags=["c"]).count()
    assert count == 0

    user.tags = ["c"]
    user.save()

    count = User.objects(tags=["c"]).count()
    assert count == 1

    # delete
    user.delete()
    count = User.objects(tags=["c"]).count()
    assert count == 0
