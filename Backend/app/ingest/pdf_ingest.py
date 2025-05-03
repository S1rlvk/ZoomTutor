import pdfplumber, os # type: ignore
from openai import OpenAI # type: ignore
from ..db import SessionLocal, Chunk
from ..utils.chunker import split_text

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ingest_pdf(doc_id: str, path: str):
    db = SessionLocal()
    with pdfplumber.open(path) as pdf:
        full_text = "\n".join(p.page.extract_text() or "" for p in pdf.pages)
    for chunk in split_text(full_text, max_tokens=1000):
        embedding = client.embeddings.create(
            model="o3-embed",
            input=chunk
        ).data[0].embedding
        db.add(Chunk(doc_id=doc_id, content=chunk, emb=embedding))
    db.commit()
