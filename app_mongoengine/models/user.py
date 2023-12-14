import attr
from app_mongoengine.from_attrs import from_attrs
from mongoengine import Document, StringField, BooleanField, IntField, ListField


# @attr.define(slots=True)
# class User:
#     user_id: str
#     name: str
#     age: int | None
#     is_active: bool
#     tags: list[str | None]


# @from_attrs(User, primary_key="name")
class User(Document):
    name = StringField(max_length=200)
    Age = IntField
    is_active = BooleanField(default=False)
    tags = ListField(default=[])
