from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.db import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from app.routers.po import router as po_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ProcurementERP - Manage Purchase Orders")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(po_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev ke liye (production me specific origin)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", include_in_schema=False)
def root_redirect():
    return {"message": "Go to /po/manage to use Manage Purchase Orders UI"}
