from docxtpl import DocxTemplate
import io

def generate_pdd_docx(pdd_text: str, project_type: str):
    """Insert generated text into your official Gold Standard PDD template"""
    template_path = "T-PreReview_V1.5-Project-Design-Document.docx"
    doc = DocxTemplate(template_path)
    doc.render({"project_type": project_type, "ai_text": pdd_text})
    buf = io.BytesIO()
    doc.save(buf)
    buf.seek(0)
    return buf
