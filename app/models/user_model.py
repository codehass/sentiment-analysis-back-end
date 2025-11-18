from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base


class User(Base):
    __tablename__ = "users"

    id = (Column(Integer, primary_key=True, index=True),)
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
