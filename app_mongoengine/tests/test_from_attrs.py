# import attr
# import pytest


# from app_mongoengine.models.user import DocumentUser, User


# def test_from_attrs(data_regression):
#     user_attrs_instance = User(
#         user_id="123",
#         name="John",
#         age=25,
#         is_active=True,
#         tags=["tag1", "tag2"],
#     )

#     document_user_instance = DocumentUser(user_attrs_instance)
#     data_regression.check(document_user_instance.__dict__)


# def test_from_attrs_wrong_attr():
#     # Example usage

#     @attr.define(slots=True)
#     class AnotherObject:
#         is_active: bool
#         tags: list[str | None]

#     # Example of usage
#     another_instance = AnotherObject(
#         is_active=True,
#         tags=["tag1", "tag2"],
#     )

#     with pytest.raises(
#         TypeError, match="Expected an instance of User, but got AnotherObject"
#     ):
#         DocumentUser(another_instance)


# # def test_from_attrs_to_attrs(data_regression):
# #     user_attrs_instance = User(
# #         user_id="123",
# #         name="John",
# #         age=25,
# #         is_active=True,
# #         tags=["tag1", "tag2"],
# #     )

# #     document_user_instance = DocumentUser(user_attrs_instance)

# #     new_user_attrs_instance = document_user_instance.to_attrs()
# #     data_regression.check(cattrs.unstructure(new_user_attrs_instance))
