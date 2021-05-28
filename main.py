from fastapi import FastAPI
import uvicorn
import models
from database import SessionLocal, engine

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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)