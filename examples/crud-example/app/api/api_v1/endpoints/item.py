from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Item])
def read_items(db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100) -> Any:
    items = crud.item.get_multi(db, skip=skip, limit=limit)
    return items

@router.get("/{id}", response_model=schemas.Item)
def read_item(*, db: Session = Depends(deps.get_db), id: int) -> Any:
    item = crud.item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/", response_model=schemas.Item, status_code=201)
def create_item(*, db: Session = Depends(deps.get_db), item_in: schemas.ItemCreate) -> Any:
    return crud.item.create(db, obj_in=item_in)

@router.put("/{id}", response_model=schemas.Item)
def update_item(*, db: Session = Depends(deps.get_db), id: int, item_in: schemas.ItemUpdate) -> Any:
    item = crud.item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return crud.item.update(db=db, db_obj=item, obj_in=item_in)

@router.delete("/{id}")
def delete_item(*, db: Session = Depends(deps.get_db), id: int) -> Any:
    item = crud.item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    crud.item.remove(db=db, id=id)
    return Response(status_code=204)