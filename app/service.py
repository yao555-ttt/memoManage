from app.models import Memo
from app.pydantic import MemoCreate,MemoUpdate,MemoRead
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException, status

class MemoService:
    @staticmethod
    def get_memo(db:Session,page:int=1,size:int=10):
        offset=(page-1)*size
        m=db.query(Memo).offset(offset).limit(size).all()
        return m
    @staticmethod
    def add_memo(db:Session,form:MemoCreate):
        m=Memo(**form.model_dump())
        db.add(m)
        db.commit()
        db.refresh(m)
        return m
    
    @staticmethod
    def update_memo(db:Session,form:MemoUpdate,id:int):
        m=db.query(Memo).get(id)
        if not m:
            raise HTTPException(status_code=404,detail='备忘录不存在')
        for k,v in form.model_dump().items():
            setattr(m,k,v)
        db.commit()
        db.refresh(m)
        return m
    @staticmethod
    def delete_memo(db:Session,id:int):
        m=db.query(Memo).get(id)
        if not m:
            raise HTTPException(status_code=404,detail='备忘录不存在')
        db.delete(m)
        db.commit()
        return {"message":"删除成功"}
    @staticmethod
    def get_memoid(db:Session,id:int):
        m=db.query(Memo).get(id)
        if not m:
            raise HTTPException(status_code=404,detail='备忘录不存在')
        return m
    
    