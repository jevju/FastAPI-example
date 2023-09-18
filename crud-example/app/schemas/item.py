from pydantic import BaseModel
from typing import Optional

# Shared properties
class ItemBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

# Properties to receive on item creation
class ItemCreate(ItemBase):
    # title: str
    pass

# Properties to receive on item update
class ItemUpdate(ItemBase):
    pass

# Properties shared by models stored in DB
class ItemInDBBase(ItemBase):
    id: int

    class Config:
        from_attributes = True

# Properties to return to client
class Item(ItemInDBBase):
    pass

# Properties stored in DB
class ItemInDB(ItemInDBBase):
    pass