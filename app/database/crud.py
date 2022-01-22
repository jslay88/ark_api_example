import logging
from datetime import datetime
from typing import List, Optional, Tuple, Union
from uuid import UUID, uuid4

from sqlalchemy.orm import Session

from . import models, schemas


logger = logging.getLogger(__name__)


"""
Helpers
"""


def _update_object(obj, update: dict, excluded_keys: List = None):
    for k, v in update.items():
        if excluded_keys and k in excluded_keys:
            continue
        setattr(obj, k, v)
    return obj


"""
Server CRUD
"""


def get_server(db: Session, _id: Union[str, UUID]) -> Optional[models.Server]:
    return db.query(models.Server).filter(models.Server.id == _id).first()


def get_servers(db: Session) -> List[models.Server]:
    return db.query(models.Server).all()


def create_or_update_server(db: Session, server: schemas.ServerUpdate) -> models.Server:
    _server = get_server(db, server.id)
    if _server is None:
        _server = models.Server(**server.dict())
        db.add(_server)
    else:
        _update_object(_server, server.dict())
        _server.updated = datetime.utcnow()  # Ensure timestamp gets updated.
    db.commit()
    return _server
