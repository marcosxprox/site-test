import os
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database
from passlib.context import CryptContext
import requests

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Verificar captcha v3
    recaptcha_secret = os.getenv("RECAPTCHA_SECRET")
    res = requests.post(
        "https://www.google.com/recaptcha/api/siteverify",
        data={"secret": recaptcha_secret, "response": user.token}
    )
    result = res.json()

    # Verifica sucesso e score mínimo
    if not result.get("success") or result.get("score", 0) < 0.5:
        raise HTTPException(status_code=400, detail="Captcha inválido ou suspeito")

    # Hashear senha
    hashed = pwd_context.hash(user.password)

    # Criar usuário
    new_user = models.User(
        username=user.username,
        email=user.email,
        password_hash=hashed
    )

    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
    except:
        db.rollback()
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")

    return new_user
