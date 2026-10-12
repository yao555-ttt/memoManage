from fastapi import APIRouter,Depends
from app.models import Memo
from app.pydantic import MemoCreate,MemoUpdate,MemoRead
from app.yilai import get_db,settings
from sqlalchemy.orm import Session
from app.service import MemoService

router=APIRouter(prefix='/mome')

@router.get('/list')
def get_m(
    db:Session=Depends(get_db),
    page:int=1,
    size:int=10
):
    return MemoService.get_memo(db,page,size)
@router.post('/add',response_model=MemoRead,status_code=201)
def add_m(
    memo:MemoCreate,
    db:Session=Depends(get_db)
):
    return MemoService.add_memo(db,memo)
@router.put('/update/{id}',response_model=MemoRead)
def update_m(
    id:int,
    memo:MemoUpdate,
    db:Session=Depends(get_db)
):
    return MemoService.update_memo(db,id,memo)
@router.delete('/delete/{id}')
def delete_m(
    id:int,
    db:Session=Depends(get_db)
):
    return MemoService.delete_memo(db,id)
@router.get('/{id}')
def get_mod(
    id:int,
    db:Session=Depends(get_db)
):
    return MemoService.get_memoid(db,id)
