# MongoDB Studies

Check the different alternatives for using mongodb

### SQLAlchemy notes

I is actually not possible to natively write sqlalchemy with mongo db,
but there's the [cData paid alternative](https://www.cdata.com/drivers/mongodb/order/python/#server)

so, this repo will use PyMongo and mongoengine for testing purposes

## [Pymongo](https://pymongo.readthedocs.io)

is a raw implementation of the mongo connection and operations

## [mongoengine](https://docs.mongoengine.org/)

ORM built over pymongo, according to [pymongo docs](https://pymongo.readthedocs.io/en/stable/tools.html):

```
MongoEngine is another ORM-like layer on top of PyMongo. It allows you to define schemas for documents and query collections using syntax inspired by the Django ORM.
```
