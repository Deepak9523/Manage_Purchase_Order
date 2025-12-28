from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.db import get_db
from app.models import PurchaseOrder, POTrack, POReceipt, POStatus
from app.schemas import POCreate, POTrackCreate, POReceiptCreate, PODetailOut

router = APIRouter(prefix="/po", tags=["Purchase Orders"])
templates = Jinja2Templates(directory="app/templates")

@router.get("/manage", response_class=HTMLResponse)
def manage_po_ui(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@router.post("/create", response_model=dict)
def create_po(payload: POCreate, db: Session = Depends(get_db)):
    po = PurchaseOrder(
        product_name=payload.product_name,
        quantity=payload.quantity,
        unit_price=payload.unit_price,
        supplier=payload.supplier
    )
    db.add(po)
    db.commit()
    db.refresh(po)
    return {"message": "PO created", "po_id": po.id}

@router.get("/create", response_class=HTMLResponse)
def create_po_form(request: Request):
    return templates.TemplateResponse("po_create.html", {"request": request})

@router.post("/track", response_model=dict)
def track_po(payload: POTrackCreate, db: Session = Depends(get_db)):
    po = db.query(PurchaseOrder).filter(PurchaseOrder.id == payload.po_id).first()
    if not po:
        raise HTTPException(status_code=404, detail="PO not found")

    track = POTrack(po_id=payload.po_id, status_update=payload.status_update, comment=payload.comment)

    # Update status if matches known workflow stages
    normalized = payload.status_update.strip().lower()
    status_map = {
        "pending": POStatus.Pending,
        "approved": POStatus.Approved,
        "dispatched": POStatus.Dispatched,
        "delivered": POStatus.Delivered,
        "received": POStatus.Received,
        "cancelled": POStatus.Cancelled
    }
    if normalized in status_map:
        po.status = status_map[normalized]

    db.add(track)
    db.commit()
    db.refresh(po)
    return {"message": "PO tracked", "po_id": po.id, "status": po.status.value}

@router.get("/track", response_class=HTMLResponse)
def track_po_form(request: Request):
    return templates.TemplateResponse("po_track.html", {"request": request})

@router.post("/receipt", response_model=dict)
def confirm_receipt(payload: POReceiptCreate, db: Session = Depends(get_db)):
    po = db.query(PurchaseOrder).filter(PurchaseOrder.id == payload.po_id).first()
    if not po:
        raise HTTPException(status_code=404, detail="PO not found")

    receipt = POReceipt(
        po_id=payload.po_id,
        received_quantity=payload.received_quantity,
        received_by=payload.received_by,
        notes=payload.notes
    )
    # Optional: update status to Received if fully received
    if payload.received_quantity >= po.quantity:
        po.status = POStatus.Received

    db.add(receipt)
    db.commit()
    db.refresh(po)
    return {"message": "PO receipt confirmed", "po_id": po.id, "status": po.status.value}

@router.get("/receipt", response_class=HTMLResponse)
def receipt_form(request: Request):
    return templates.TemplateResponse("po_receipt.html", {"request": request})

@router.get("/{po_id}", response_model=PODetailOut)
def get_po_detail(po_id: int, db: Session = Depends(get_db)):
    po = db.query(PurchaseOrder).filter(PurchaseOrder.id == po_id).first()
    if not po:
        raise HTTPException(status_code=404, detail="PO not found")
    return po
