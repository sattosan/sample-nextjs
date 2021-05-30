from sqlalchemy.orm import Session

import models
import schemas


def get_all(db: Session):
    db_posts = db.query(models.post.Post).all()
    return db_posts


def create(db: Session, post: schemas.post.PostCreate):
    """create post by title and content"""
    db_post = models.post.Post(title=post.title, content=post.content)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def delete(db: Session, id: int):
    """delete post by id"""
    db_post = db.query(models.post.Post).filter(models.post.Post.id == id).first()
    db.delete(db_post)
    db.commit()
    return db_post
