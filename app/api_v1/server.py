from typing import List, Union
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import crud, get_db, models, schemas


router = APIRouter()


@router.get('/', response_model=schemas.ServerListWithModIdentifier)
def get_servers(db: Session = Depends(get_db)):
    return schemas.ServerListWithModIdentifier(servers=crud.get_servers(db))


@router.get('/{server_id}', response_model=schemas.ServerDB)
def get_server(server_id: UUID, db: Session = Depends(get_db)):
    return crud.get_server(db, server_id)


@router.post('/', response_model=schemas.ServerDBWithModIdentifier)
def create_or_update_server(server: schemas.ServerUpdate, db: Session = Depends(get_db)):
    return crud.create_or_update_server(db, server)
