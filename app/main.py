from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from authentication.auth import get_password_hash
from schemas.user_schema import UserSchema, UserCreate
from models.user_model import User
from db.database import engine, Base, get_db

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/users/", response_model=UserSchema)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username, email=user.email, hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


@app.get("/")
def get_home():
    return {"message": "Hello from backend"}
