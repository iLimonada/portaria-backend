# models.py
from sqlalchemy import Column, Integer, String
from db.database import Base

class ResidentModel(Base):
    __tablename__ = "residents"  # Mudou de moradores para residents

    id = Column(Integer, primary_key=True, index=True)
    resident_name = Column(String, index=True, nullable=False)
    apartment = Column(String, index=True, nullable=False)
    block = Column(String, index=True, nullable=False)
    relatives = Column(String, nullable=True) 
    cleaner = Column(String, nullable=True)    