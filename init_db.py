# from app.db import engine, Base
# from app.models import CommThread, CommMessage
# from app.models import CommThread, CommMessage


# def init_db():
#     print("Creating database tables...")
#     Base.metadata.create_all(bind=engine)
#     print("Database tables created successfully!")

# if __name__ == "__main__":
#     init_db()

# End Code 

# init_db.py
# from app.db import Base, engine
# from app.models import PurchaseOrder, POTrack, POReceipt

# def init():
#     print("Creating database tables...")
#     Base.metadata.create_all(bind=engine)
#     print("✅ Tables created successfully!")

# if __name__ == "__main__":
#     init()

from app.db import Base, engine
from app.models import PurchaseOrder, POTrack, POReceipt

Base.metadata.create_all(bind=engine)

print("✅ Database tables created successfully")

