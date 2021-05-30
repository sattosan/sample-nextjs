from sqlalchemy.orm import Session
from hashlib import md5 as hash_func

import models
import schemas


def get_all(db: Session):
    db_users = db.query(models.user.User).all()
    return db_users


def create(db: Session, user: schemas.user.UserCreate):
    """create user by name and password"""
    hashed_password = hash_func(user.password.encode()).hexdigest()
    db_user = models.user.User(name=user.name, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete(db: Session, name: str):
    """delete user by name"""
    db_user = db.query(models.user.User).filter(models.user.User.name == name).first()
    db.delete(db_user)
    db.commit()
    return db_user
