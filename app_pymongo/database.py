from pymongo import MongoClient

DATABASE_HOST = "localhost"
DATABASE_PORT = "27027"
DATABASE_USER = "root"
DATABASE_PASSWORD = "pass"
DATABASE_NAME = "mydatabase"

CONNECTION_STRING = f"mongodb://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}?authSource=admin&retryWrites=true&w=majority"
# CONNECTION_STRING = f"mongodb:///?Server={DATABASE_HOST}&Port={DATABASE_PORT}&Database={DATABASE_NAME}&User={DATABASE_USER}&Password={DATABASE_PASSWORD}"

# client = MongoClient(
#     f"mongodb://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/",
#     authSource="admin",
# )
client = MongoClient(CONNECTION_STRING)
database = client[DATABASE_NAME]
