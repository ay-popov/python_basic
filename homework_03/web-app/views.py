from fastapi import APIRouter
from pydantic import BaseModel
from typing import Union

router = APIRouter(tags=["Ping"], prefix="/ping")


class Item(BaseModel):
    name: str
    price: float


@router.get("")
def get_items():
    return {"message": "pong"}


@router.post("")
def create_item(data: Item):
    return {"data": data}


@router.put("{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
