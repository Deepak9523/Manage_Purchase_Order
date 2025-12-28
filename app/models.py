from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db import Base
import enum

class POStatus(enum.Enum):
    Pending = "Pending"
    Approved = "Approved"
    Dispatched = "Dispatched"
    Delivered = "Delivered"
    Received = "Received"
    Cancelled = "Cancelled"

class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    supplier = Column(String, nullable=False)
    status = Column(Enum(POStatus), default=POStatus.Pending, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    tracks = relationship("POTrack", back_populates="po", cascade="all, delete-orphan")
    receipts = relationship("POReceipt", back_populates="po", cascade="all, delete-orphan")

class POTrack(Base):
    __tablename__ = "po_tracks"

    id = Column(Integer, primary_key=True, index=True)
    po_id = Column(Integer, ForeignKey("purchase_orders.id"), nullable=False)
    status_update = Column(String, nullable=False)
    comment = Column(String, nullable=True)
    updated_at = Column(DateTime, default=datetime.utcnow)

    po = relationship("PurchaseOrder", back_populates="tracks")

class POReceipt(Base):
    __tablename__ = "po_receipts"

    id = Column(Integer, primary_key=True, index=True)
    po_id = Column(Integer, ForeignKey("purchase_orders.id"), nullable=False)
    received_quantity = Column(Integer, nullable=False)
    received_by = Column(String, nullable=False)
    notes = Column(String, nullable=True)
    received_at = Column(DateTime, default=datetime.utcnow)

    po = relationship("PurchaseOrder", back_populates="receipts")
