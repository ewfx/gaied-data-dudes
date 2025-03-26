#  GenAI Email Classification & OCR Pipeline

##  Project Summary

This project offers a robust and modular pipeline for automated email classification and content extraction. By combining **zero-shot NLP techniques** with **OCR-based document parsing**, it streamlines email processing workflows in enterprise environments.

---

##  Key Features

- ** Zero-Shot Classification**  
  Instantly categorize email content into predefined request types using `roberta-large-mnli` without requiring labeled training data.

- ** OCR Integration**  
  Extracts text from image-based PDF attachments using Tesseract OCR.

- ** Attachment Parsing**  
  Supports `.pdf`, `.docx`, and image-based documents with fallback OCR handling.

- **FastAPI REST API**  
  Interactive REST endpoints for integration with external systems.

- ** Modular Design**  
  Clean, maintainable architecture suitable for scaling and team collaboration.

---

##  Folder Structure

```bash
my_ocr_pipeline/
├── requirements.txt
├── Dockerfile            (optional: demonstrates containerization)
├── README.md             (optional: project instructions)
├── src/
│   ├── __init__.py
│   ├── email_parser.py
│   ├── attachment_extractor.py
│   ├── classification.py
│   ├── domain_rules.py
│   ├── field_extraction.py
│   ├── duplicate_check.py
│   └── pipeline.py
├── scripts/
│   ├── generate_samples.py
│   └── run_pipeline.py
└── test_emails/          (generated or provided .eml sample files)
```

---

##  Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```
---

### Generate Sample Emails (Optional)
```bash
python scripts/generate_samples.py
```
### Run Pipeline

CLI Mode

```bash
python scripts/run_pipeline.py
```
API Mode (FastAPI)

```bash
python scripts/serve_api.py
```
---
### Visit Swagger UI for interactive API testing.

Example Output
```bash
{
  "filename": "email_inbound_scanned.eml",
  "primary_request_type": {
    "label": "Money Movement-Inbound",
    "confidence": 0.95,
    "reasoning": "Detected Money Movement-Inbound with domain rules."
  },
  "sub_request_types": [
    {"label": "Fee Payment", "confidence": 0.75}
  ],
  "extracted_fields": {"amount": "$2,500,000", "deal_name": null, "expiration_date": null},
  "duplicate_flag": false,
  "duplicate_reason": ""
}
```
---
### Technologies Used

- ** NLP: Zero-Shot Classification (Roberta-large-mnli)

- ** OCR: Tesseract

- ** Web API: FastAPI

- ** Attachments: PyPDF2, pdf2image, python-docx
---
### API Usage Example (cURL)

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/classify_eml' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'eml_file=@email_adjustment_textpdf.eml;type=message/rfc822'
```
---
