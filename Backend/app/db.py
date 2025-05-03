import os
from sqlalchemy import create_engine, Column, Integer, String # type: ignore
from sqlalchemy.orm import sessionmaker, declarative_base # type: ignore
from pgvector.sqlalchemy import Vector # type: ignore

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


class Chunk(Base):
    __tablename__ = "chunks"
    id      = Column(Integer, primary_key=True, index=True)
    doc_id  = Column(String, index=True)
    content = Column(String)
    emb     = Column(Vector(1536))          # 1 536-dim OpenAI embedding
