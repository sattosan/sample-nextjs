from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql.functions import current_timestamp

from database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    title = Column(String, nullable=False, index=True)
    content = Column(String, nullable=False, index=True)
    created_at = Column(DateTime, nullable=False, server_default=current_timestamp())
