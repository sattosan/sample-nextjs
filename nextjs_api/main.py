from typing import Generator

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from crud import crud_user, crud_post
import database
import schemas

# table作成
database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db() -> Generator:
    try:
        db = database.SessionLocal()  # sessionを生成
        yield db
    finally:
        db.close()


# ユーザ全件取得
@app.get("/users/", response_model=schemas.user.UserList)
def read_users(db: Session = Depends(get_db)):
    return crud_user.get_all(db=db)


# ユーザ登録
@app.post("/api/register/", response_model=schemas.user.User)
def create_user(user: schemas.user.UserCreate, db: Session = Depends(get_db)):
    return crud_user.create(db=db, user=user)


# ユーザ削除
@app.delete("/users/{name}", response_model=schemas.user.User)
def delete_user(name: str, db: Session = Depends(get_db)):
    return crud_user.delete(db=db, name=name)


# ポスト全件取得
@app.get("/list-post/")
def read_posts(db: Session = Depends(get_db)):
    return crud_post.get_all(db=db)


# ポスト投稿
@app.post("/posts/create/", response_model=schemas.post.Post)
def create_post(post: schemas.post.PostCreate, db: Session = Depends(get_db)):
    return crud_post.create(db=db, post=post)


# ポスト削除
@app.delete("/posts/{int}", response_model=schemas.post.Post)
def delete_post(id: int, db: Session = Depends(get_db)):
    return crud_post.delete(db=db, id=id)
