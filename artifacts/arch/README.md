
# GenAI Email Classification and OCR Pipeline

A production-ready, modular Python pipeline for classifying emails, extracting key fields, and performing OCR on attachments. The system leverages zero-shot classification (using roberta-large-mnli) and domain-specific logic to accurately process and classify email content. A REST API built with FastAPI provides easy integration, along with automatic documentation via Swagger.

---

## System Overview

This pipeline automates email processing by parsing .eml files, extracting textual content from emails and attachments (including PDFs and DOCX files), performing OCR for image-based documents, classifying the content into predefined request types, applying domain-specific rules for prioritization, and extracting key data fields (like amounts). The system is designed for ease of use, modularity, and scalability, making it suitable for enterprise-level email automation tasks.

---


## Folder Structure

```bash
my_ocr_pipeline/
├── requirements.txt
├── README.md
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
│   ├── run_pipeline.py
│   └── serve_api.py
└── test_emails/  # Sample .eml files
```
src/: Core modules for parsing, OCR, classification, and field extraction.

scripts/: Utility scripts for running and serving the pipeline.

test_emails/: Directory containing example .eml files for testing.

## Installation

### System Dependencies

Make sure you have Tesseract installed on your system for OCR capabilities:


### Python Dependencies

Install Python dependencies:
```bash
pip install -r requirements.txt
```

Usage

Run the Pipeline Locally

To process .eml files in batch:
```bash
python scripts/generate_samples.py  # (Optional) Generate sample emails
python scripts/run_pipeline.py
```
The output will be printed as a JSON report to the console.

### REST API

Start the FastAPI server:
```bash
python scripts/serve_api.py
```
The API will be available at http://localhost:8000/docs.

#### API Endpoint

POST /classify_eml: Upload an .eml file and receive classification results.

Example Input/Output

Input (sample.eml)

Upload via API (POST /classify_eml):

POST /classify_eml
Content-Type: multipart/form-data
File: sample.eml

#### Output (JSON Response)
```bash
{
  "filename": "sample.eml",
  "primary_request_type": {
    "label": "Money Movement-Inbound",
    "confidence": 0.95,
    "reasoning": "Detected Money Movement-Inbound with highest confidence; domain rules applied."
  },
  "sub_request_types": [
    {
      "label": "Fee Payment",
      "confidence": 0.75
    }
  ],
  "extracted_fields": {
    "deal_name": null,
    "amount": "$2,500,000",
    "expiration_date": null
  },
  "duplicate_flag": false,
  "duplicate_reason": ""
}
```
## Architecture Overview

The following diagram outlines the core data flow:

```bash
.eml Upload ─> Parsing ─> OCR ─> Classification ─> Domain Logic ─> JSON Output
                      │                             ^
                      └───> Key Field Extraction ────┘
```
-- Parsing: Extracts email metadata and text.

-- OCR: Converts images and scanned PDFs into text.

-- Classification: Performs zero-shot classification of content.

-- Domain Logic: Prioritizes labels based on custom business rules.

-- Key Field Extraction: Identifies key fields such as monetary amounts.
