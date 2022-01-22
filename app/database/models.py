from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID

from . import Base


class CreationDateMixIn(object):
    created = Column(DateTime, server_default=func.now(), nullable=False)


"""
Server Model
"""


class Server(Base, CreationDateMixIn):
    __tablename__ = 'server'

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    updated = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    name = Column(VARCHAR(63), nullable=False)
    version = Column(VARCHAR(12), nullable=False)
