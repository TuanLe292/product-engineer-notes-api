from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from core.deps import get_db
from core.database import Base, engine
from models import user, note

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health(db: Session = Depends(get_db)):
    return {"status": "ok"}