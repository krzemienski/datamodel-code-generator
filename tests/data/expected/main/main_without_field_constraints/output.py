# generated by datamodel-codegen:
#   filename:  api_constrained.yaml
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import AnyUrl, BaseModel, Field, conint, constr


class Pet(BaseModel):
    id: conint(ge=0)
    name: constr(max_length=256)
    tag: Optional[constr(max_length=64)] = None


class Pets(BaseModel):
    __root__: List[Pet] = Field(..., max_items=10, min_items=1)


class UID(BaseModel):
    __root__: conint(ge=0)


class Phone(BaseModel):
    __root__: constr(min_length=3)


class User(BaseModel):
    id: conint(ge=0)
    name: constr(max_length=256)
    tag: Optional[constr(max_length=64)] = None
    uid: UID
    phones: Optional[List[Phone]] = Field(None, max_items=10)
    fax: Optional[List[constr(min_length=3)]] = None


class Users(BaseModel):
    __root__: List[User]


class Id(BaseModel):
    __root__: str


class Rules(BaseModel):
    __root__: List[str]


class Error(BaseModel):
    code: int
    message: str


class Api(BaseModel):
    apiKey: Optional[str] = Field(
        None, description='To be used as a dataset parameter value'
    )
    apiVersionNumber: Optional[str] = Field(
        None, description='To be used as a version parameter value'
    )
    apiUrl: Optional[AnyUrl] = Field(
        None, description="The URL describing the dataset's fields"
    )
    apiDocumentationUrl: Optional[AnyUrl] = Field(
        None, description='A URL to the API console for each API'
    )


class Apis(BaseModel):
    __root__: List[Api]


class Event(BaseModel):
    name: Optional[str] = None


class Result(BaseModel):
    event: Optional[Event] = None
