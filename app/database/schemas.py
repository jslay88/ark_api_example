from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel, Field

from ..settings import settings


class CreationDateMixin(BaseModel):
    created: datetime


class ModIdentifierMixin(BaseModel):
    mod_id: str = settings.MOD_IDENTIFIER


class ServerBase(BaseModel):
    id: UUID
    name: str = Field(min_length=1, max_length=63, description='Game Server Name')
    version: str = Field(min_length=1, max_length=12, description='Game Server Version')

    class Config:
        orm_mode = True


class ServerDB(ServerBase, CreationDateMixin):
    updated: datetime


class ServerDBWithModIdentifier(ServerDB, ModIdentifierMixin):
    pass


class ServerUpdate(ServerBase):
    pass


class ServerList(BaseModel):
    servers: List[ServerDB]


class ServerListWithModIdentifier(ServerList, ModIdentifierMixin):
    pass
