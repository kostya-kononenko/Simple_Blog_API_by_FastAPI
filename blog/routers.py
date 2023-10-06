from fastapi import APIRouter, Depends

from .import crud
from .schemas import PostBase
from sqlalchemy.orm import Session
from database.database import get_db

router = APIRouter(
  prefix='/post',
  tags=['post']
)


@router.post('')
def create(request: PostBase, db: Session = Depends(get_db)):
    return crud.create(db, request)


@router.get('/all')
def posts(db: Session = Depends(get_db)):
    return crud.get_all(db)
