from sqlalchemy import Column, String, Integer
from database import Base

class Test(Base):

    __tablename__ = "test"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
