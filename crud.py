from sqlalchemy.orm import Session
import models

def insert_test(db: Session, name: str):
    db_model = models.Test(
        name=name
    )

    db.add(db_model)
    db.flush()
    return True

def select_all_test(db: Session):
    query = db.query(models.Test)
    return query.all()