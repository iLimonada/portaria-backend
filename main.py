from fastapi import FastAPI, Depends, HTTPException, status, Response
from typing import List
from sqlalchemy.orm import Session

from db.database import engine, get_db
from models import models
from schemas import schemas

# Cria as tabelas no banco de dados caso elas não existam
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Condo Management API", version="0.1.0")

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API do Portaria Backend!"}

# GET: Lista todos os moradores cadastrados
@app.get("/residents", response_model=List[schemas.ResidentResponse])
def get_residents(db: Session = Depends(get_db)):
    db_residents = db.query(models.ResidentModel).all()
    return db_residents

# POST: Cria um novo morador (retorna 201 Created com os dados do novo morador)
@app.post("/residents", response_model=schemas.ResidentResponse, status_code=status.HTTP_201_CREATED)
def create_resident(resident: schemas.ResidentCreate, db: Session = Depends(get_db)):
    new_resident = models.ResidentModel(
        resident_name=resident.resident_name,
        apartment=resident.apartment,
        block=resident.block,
        relatives=resident.relatives,
        cleaner=resident.cleaner
    )

    db.add(new_resident)
    db.commit()
    db.refresh(new_resident)

    return new_resident

# PUT: Atualiza os dados de um morador existente (retorna 404 se não for encontrado)
@app.put("/residents/{resident_id}", response_model=schemas.ResidentResponse)
def update_resident(resident_id: int, resident_updated: schemas.ResidentCreate, db: Session = Depends(get_db)):
    db_resident = db.query(models.ResidentModel).filter(models.ResidentModel.id == resident_id).first()

    if not db_resident:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Morador não encontrado")
    
    db_resident.resident_name = resident_updated.resident_name
    db_resident.apartment = resident_updated.apartment
    db_resident.block = resident_updated.block
    db_resident.relatives = resident_updated.relatives
    db_resident.cleaner = resident_updated.cleaner

    db.commit()
    db.refresh(db_resident)

    return db_resident

# DELETE: Remove um morador do banco se ele existir (retorna 204 No Content se der certo ou 404 se não encontrar)
@app.delete("/residents/{resident_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_resident(resident_id: int, db: Session = Depends(get_db)):
    db_resident = db.query(models.ResidentModel).filter(models.ResidentModel.id == resident_id).first()

    if not db_resident:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Morador não encontrado")
    
    db.delete(db_resident)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)