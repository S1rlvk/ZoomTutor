from fastapi import FastAPI # type: ignore
from .db import Base, engine

app = FastAPI(title="ZoomTutor backend")

Base.metadata.create_all(bind=engine)      # create tables once


@app.get("/health")
def health():
    return {"status": "ok"}


from fastapi import FastAPI, UploadFile, BackgroundTasks # type: ignore
from .db import Base, engine
from .ingest.pdf_ingest import ingest_pdf

app = FastAPI(title="ZoomTutor backend")
Base.metadata.create_all(bind=engine)


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ingest/pdf")
async def ingest_pdf_endpoint(
    file: UploadFile,
    tasks: BackgroundTasks
):
    # save temp file first
    tmp_path = f"/tmp/{file.filename}"
    with open(tmp_path, "wb") as f:
        f.write(await file.read())

    doc_id = file.filename
    tasks.add_task(ingest_pdf, doc_id, tmp_path)
    return {"status": "queued", "doc_id": doc_id}
