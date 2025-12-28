# First Code 
# from typing_extensions import Annotated
# from pydantic import BaseModel, Field, conint, confloat
# from typing import List, Optional
# from datetime import datetime

# class POCreate(BaseModel):
#     product_name: str = Field(..., min_length=1)
#     quantity: conint(gt=0)
#     unit_price: confloat(gt=0)
#     supplier: str = Field(..., min_length=1)

# class POBase(BaseModel):
#     id: int
#     product_name: str
#     quantity: int
#     unit_price: float
#     supplier: str
#     status: str
#     created_at: datetime

#     class Config:
#         from_attributes = True

# class POTrackCreate(BaseModel):
#     po_id: int
#     status_update: str
#     comment: Optional[str] = None

# class POReceiptCreate(BaseModel):
#     po_id: int
#     received_quantity: conint(gt=0)
#     received_by: str
#     notes: Optional[str] = None

# class POTrackOut(BaseModel):
#     status_update: str
#     comment: Optional[str] = None
#     updated_at: datetime

#     class Config:
#         from_attributes = True

# class POReceiptOut(BaseModel):
#     received_quantity: int
#     received_by: str
#     notes: Optional[str]
#     received_at: datetime

#     class Config:
#         from_attributes = True

# class PODetailOut(POBase):
#     tracks: List[POTrackOut] = []
#     receipts: List[POReceiptOut] = []

# END Code

from typing_extensions import Annotated
from pydantic import BaseModel, Field, conint, confloat
from typing import List, Optional
from datetime import datetime

class POCreate(BaseModel):
    product_name: str = Field(..., min_length=1)
    quantity: Annotated[int, conint(gt=0)]
    unit_price: Annotated[float, confloat(gt=0)]
    supplier: str = Field(..., min_length=1)

class POBase(BaseModel):
    id: int
    product_name: str
    quantity: int
    unit_price: float
    supplier: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True

class POTrackCreate(BaseModel):
    po_id: int
    status_update: str
    comment: Optional[str] = None

class POReceiptCreate(BaseModel):
    po_id: int
    received_quantity: Annotated[int, conint(gt=0)]
    received_by: str
    notes: Optional[str] = None

class POTrackOut(BaseModel):
    status_update: str
    comment: Optional[str] = None
    updated_at: datetime

    class Config:
        from_attributes = True

class POReceiptOut(BaseModel):
    received_quantity: int
    received_by: str
    notes: Optional[str]
    received_at: datetime

    class Config:
        from_attributes = True

class PODetailOut(POBase):
    tracks: List[POTrackOut] = []
    receipts: List[POReceiptOut] = []
