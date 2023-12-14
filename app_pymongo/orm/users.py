# from sqlalchemy import Table, Column, Integer, String

# from models.user import User
# from app.orm.database import mapper_registry


# user_table = Table(
#     "users",
#     mapper_registry.metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String(50)),
#     Column("email", String(255), unique=True),
#     Column("password", String(16)),
# )

# mapper_registry.map_imperatively(User, user_table)
