from typing import Any
from mongoengine import (
    Document,
    StringField,
    IntField,
    DateTimeField,
    ListField,
    BinaryField,
    BooleanField,
    DictField,
    FloatField,
    ReferenceField,
)
import attr
from datetime import datetime


# def get_attrs_type(mongoengine_field_type):
#     # Map mongoengine field types to attrs types
#     type_mapping = {
#         StringField: str,
#         IntField: int,
#         FloatField: float,
#         BooleanField: bool,
#         DateTimeField: datetime,
#         DictField: dict,
#         ListField: list,
#         BinaryField: bytes,
#         # Add more mappings as needed
#     }

#     return type_mapping.get(mongoengine_field_type, str)  # Default to str


# def to_attrs(document_instance, attrs_class):
#     # Create a dictionary of field names and their values
#     attrs_dict = {}

#     print(document_instance._data.items())
#     for field_name, field_value in document_instance._data.items():
#         field_instance = document_instance._fields.get(field_name)
#         if field_instance:
#             attrs_type = get_attrs_type(type(field_instance))
#             if attrs_type == "DocumentClass":
#                 # Handle ReferenceField by calling its to_attrs method
#                 attrs_dict[field_name] = getattr(
#                     field_value, "to_attrs", lambda: None
#                 )()
#             else:
#                 attrs_dict[field_name] = attrs_type(field_value)

#     # Filter out keys not present in the attrs class
#     valid_attrs_dict = {k: v for k, v in attrs_dict.items() if hasattr(attrs_class, k)}

#     print(valid_attrs_dict, attrs_dict.items())

#     # Create an instance of the attrs class using attr.ib
#     attrs_instance = attrs_class(**valid_attrs_dict)

#     return attrs_instance


def get_mongoengine_field_type(attr_type):
    # Map attrs types to mongoengine field types
    type_mapping = {
        str: StringField,
        int: IntField,
        float: FloatField,
        bool: BooleanField,
        datetime: DateTimeField,
        dict: DictField,
        list: ListField,
        bytes: BinaryField
        # Add more mappings as needed
    }

    return type_mapping.get(attr_type, StringField)  # Default to StringField


def from_attrs(attrs_class, primary_key=None):
    def decorator(document_class):
        class DocumentClass(Document):
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                super().__init__()
                self.setup_document()

                if isinstance(args[0], attrs_class):
                    attrs_instance = args[0]

                    # Deserialize attrs instance and set field values
                    for field_name, field_value in attr.asdict(attrs_instance).items():
                        setattr(self, field_name, field_value)
                else:
                    raise TypeError(
                        f"Expected an instance of {attrs_class.__name__}, but got {type(args[0]).__name__}"
                    )

            def setup_document(self) -> None:
                attrs_fields = attr.fields_dict(attrs_class)
                # Add fields to the mongoengine document class
                for field_name, field_info in attrs_fields.items():
                    mongoengine_field_type = get_mongoengine_field_type(field_info.type)
                    is_optional = field_info.default is attr.NOTHING

                    # If it's a List field, get the type of elements in the list
                    if field_info.type is list:
                        list_type = field_info.type
                        element_type = get_mongoengine_field_type(list_type)
                        mongoengine_field_type = ListField(
                            element_type, default=None if is_optional else []
                        )

                    # Set default to None for optional fields
                    default_value = (
                        None if is_optional else mongoengine_field_type.DEFAULT
                    )

                    # Check for ReferenceField and extract referenced_doc_class from metadata
                    if (
                        hasattr(field_info, "metadata")
                        and "reference_class" in field_info.metadata
                    ):
                        referenced_doc_class = field_info.metadata["reference_class"]
                        field_instance = ReferenceField(referenced_doc_class)
                    else:
                        field_instance = mongoengine_field_type(
                            primary_key=primary_key == field_name, default=default_value
                        )

                    setattr(self, field_name, field_instance)

            # def to_attrs(self) -> attrs_class:
            #     return to_attrs(self, attrs_class)

        return DocumentClass

    return decorator
