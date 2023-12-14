from attr import field
from attrs import define


@define
class User:
    id: str | None = field(init=False)
    name: str
    email: str
    password: str
