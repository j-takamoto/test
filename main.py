from fastapi import FastAPI, Depends
import uvicorn
import models, crud
from database import SessionLocal, engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/favicon.ico")
async def favicon():
    return True

@app.get("/")
async def index():
    return {"result": True}

@app.get("/create_test/{name}")
async def create_test(name: str, db: Session = Depends(get_db)):
    try:
        result = crud.insert_test(db, name)
        db.commit()
    finally:
        db.close()
    return {"result": result}

@app.get("/get_all_test")
async def get_all_test(db: Session = Depends(get_db)):
    try:
        result = crud.select_all_test(db)
    finally:
        db.close()
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)