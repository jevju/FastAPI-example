from sqlalchemy.orm import Session

from app.db import base
from app.db.session import engine

def init_db(db: Session) -> None:
    base.Base.metadata.create_all(bind=engine)
