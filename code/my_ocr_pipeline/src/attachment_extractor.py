# src/attachment_extractor.py

import io
from typing import List
import PyPDF2
import docx
import pytesseract
from pdf2image import convert_from_bytes
from PIL import Image

def extract_text_from_attachments(attachments: List[dict]) -> str:
    """
    For each attachment:
      - Attempt text extraction from PDF (PyPDF2).
      - If text is too short, fallback to OCR with pdf2image + pytesseract.
      - If .docx, parse with python-docx.
      - Otherwise, skip or handle custom.

    Returns concatenated text from all attachments.
    """
    full_attachment_text = ""

    for attach in attachments:
        filename = attach["filename"].lower()
        data = attach["data"]

        # PDF extraction
        if filename.endswith(".pdf"):
            text_from_pdf = ""
            try:
                pdf_file = PyPDF2.PdfReader(io.BytesIO(data))
                pdf_text_parts = []
                for page in pdf_file.pages:
                    extracted = page.extract_text()
                    if extracted:
                        pdf_text_parts.append(extracted)
                text_from_pdf = "\n".join(pdf_text_parts)
            except Exception:
                text_from_pdf = ""  # fallback below

            # If text_from_pdf is short or empty, do OCR fallback
            if len(text_from_pdf.strip()) < 30:
                try:
                    images = convert_from_bytes(data)
                    ocr_text_parts = []
                    for img in images:
                        ocr_extracted = pytesseract.image_to_string(img)
                        ocr_text_parts.append(ocr_extracted)
                    text_from_pdf = "\n".join(ocr_text_parts)
                except Exception as e:
                    text_from_pdf = f"[PDF OCR error: {e}]"

            full_attachment_text += text_from_pdf + "\n"

        # DOCX extraction
        elif filename.endswith(".docx"):
            docx_text = ""
            try:
                file_stream = io.BytesIO(data)
                doc_obj = docx.Document(file_stream)
                paragraphs = [p.text for p in doc_obj.paragraphs if p.text.strip()]
                docx_text = "\n".join(paragraphs)
            except Exception as e:
                docx_text = f"[DOCX error: {e}]"

            full_attachment_text += docx_text + "\n"

        else:
            # For other file types, skip or handle them
            pass

    return full_attachment_text
