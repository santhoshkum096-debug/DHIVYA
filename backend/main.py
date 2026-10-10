from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, Response
from pathlib import Path

from .models import DocumentRequest, ExportRequest
from .ai_service import generate_document
from .document_generator import make_pdf, make_docx, make_txt

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

app = FastAPI(title="LegalEase API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return FileResponse(FRONTEND_DIR / "index.html")

@app.get("/health")
def health():
    return {"status": "ok", "project": "LegalEase"}

@app.post("/api/generate")
def generate(request: DocumentRequest):
    try:
        content = generate_document(request)
        return {"success": True, "content": content}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

@app.post("/api/export/txt")
def export_txt(request: ExportRequest):
    return Response(
        make_txt(request.content),
        media_type="text/plain",
        headers={"Content-Disposition": "attachment; filename=LegalEase_Document.txt"},
    )

@app.post("/api/export/docx")
def export_docx(request: ExportRequest):
    return Response(
        make_docx(request.content),
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={"Content-Disposition": "attachment; filename=LegalEase_Document.docx"},
    )

@app.post("/api/export/pdf")
def export_pdf(request: ExportRequest):
    return Response(
        make_pdf(request.content),
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=LegalEase_Document.pdf"},
    )
