# Manage_Purchase_Order

This project is a Purchase Order Management System built with FastAPI (backend), PostgreSQL (database), and HTML/CSS/JS (frontend).
It provides a complete workflow for managing purchase orders:

 Create PO – Add new purchase orders with supplier and product details.

 Track PO Dispatch – Update and monitor PO status (Pending, Approved, Dispatched, Delivered, Received, Cancelled).

 PO Receipt Confirmation – Confirm received quantities and mark orders as completed.

 Dashboard – Attractive, colorful UI to view and manage all purchase orders.

# Tech Stack

Backend: FastAPI (Python)

Database: PostgreSQL (SQLAlchemy ORM)

Frontend: HTML, CSS, JavaScript (Jinja2 templates)

Environment: .env for DB credentials

# app/
├─ main.py              
├─ db.py               
├─ models.py           
├─ schemas.py          
├─ routers/
│  └─ po.py            
├─ templates/           
│  ├─ base.html       
│  ├─ po_create.html  
│  ├─ po_track.html    
│  └─ po_receipt.html   
└─ static/              
   ├─ style.css         
   └─ app.js
   
# Install dependencies
pip install -r requirements.txt

# Configure PostgreSQL
CREATE DATABASE procurement_db;

ALTER USER postgres WITH PASSWORD 'admin';

# Environment variables (.env)
POSTGRES_USER=postgres
POSTGRES_PASSWORD=admin
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=procurement_db

# Initialize DB
python init_db.py
# Usage
Dashboard: http://127.0.0.1:8000/po/manage

API Docs: http://127.0.0.1:8000/docs

# API Testing
1. PO created :-
API :-http://localhost:8000/po/create/

Post Data:- 

{

  "product_name": "Laptop1",
  
  "quantity": 10,
  
  "unit_price": 55000,
  
  "supplier": "hp"
  
}

2. PO Track

API:-http://localhost:8000/po/track/

Post Data:-

{

  "po_id": 1,
  
  "status_update": "Approved",
  
  "comment": "Approved by manager"
  
}

3. PO Recipt

API :-http://localhost:8000/po/receipt/

Post Data:-
{

  "po_id": 1,
  
  "received_quantity": 10,
  
  "received_by": "Store Manager",
  
  "notes": "All items received"
  
}

4. PO details with tracking & receipts

Get API :- http://localhost:8000/po/{id}/





# Endpoints
POST /po/create → Create new PO

POST /po/track → Update PO status

POST /po/receipt → Confirm PO receipt

GET /po/{id} → Get PO details with tracking & receipts


