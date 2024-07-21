from ninja import Schema
from pydantic import HttpUrl


class AddUrlSchema(Schema):
    url: HttpUrl
