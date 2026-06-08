from fastapi import FastAPI, Depends, HTTPException, status, Response, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session
import jwt
from datetime import datetime, timezone, timedelta

from db.database import engine, get_db
from models import models
from schemas import schemas

# Cria as tabelas no banco de dados caso elas não existam
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Portaria Management API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens (ajuste conforme necessário)
    allow_credentials=True, # Permite o envio de cookies e credenciais
    allow_methods=["*"],  # Permite todos os métodos HTTP
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

JWT_SECRET_KEY = "ChaveSecretaSuperSeguraCondominio123"
JWT_ALGORITHM = "HS256"

USER_ADMIN = "admin"
USER_PASSWORD = "portaria123"

class LoginRequest(BaseModel):
    username: str
    password: str

def verify_token(authorization: Optional[str] = Header(None)):
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Authorization header is missing"
        )
    
    try:
        token = authorization.split(" ")[1]  # Extrai o token do formato "Bearer <token>"
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload
    except Exception:
        raise HTTPException (
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

# Rota de login para obter o token JWT (retorna 200 OK com o token ou 400 Bad Request se as credenciais forem inválidas)
@app.post("/login")
def login(data: LoginRequest):
    if data.username == USER_ADMIN and data.password == USER_PASSWORD:
        payload = {
            "sub": data.username,
            "exp": datetime.now(timezone.utc) + timedelta(hours=2)
        }
        return {"token": jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)}
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, 
        detail="Invalid username or password"
    )

# Rota de teste para verificar se a API está funcionando
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
def create_resident(
        resident: schemas.ResidentCreate, 
        db: Session = Depends(get_db),
        _token: dict = Depends(verify_token)
):
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
def update_resident(
    resident_id: int, 
    resident_updated: schemas.ResidentCreate, 
    db: Session = Depends(get_db),
    _token: dict = Depends(verify_token) # Adicionado proteção aqui
):
    db_resident = db.query(models.ResidentModel).filter(models.ResidentModel.id == resident_id).first()

    if not db_resident:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resident not found")
    
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
def delete_resident(
    resident_id: int, 
    db: Session = Depends(get_db),
    _token: dict = Depends(verify_token)
):
    db_resident = db.query(models.ResidentModel).filter(models.ResidentModel.id == resident_id).first()

    if not db_resident:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resident not found")
    
    db.delete(db_resident)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)