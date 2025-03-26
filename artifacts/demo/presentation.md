# GenAI Email Classification & OCR Pipeline

## Automate email processing with advanced NLP and OCR.

### Problem Statement

-- Manual email sorting is slow and error-prone.

-- Traditional OCR solutions struggle with scanned documents.

### Solution Overview & Architecture
```bash
 Modular pipeline: Parsing → OCR → Classification → Data Extraction → API
```
#### Key Components

-- Email Parsing: Standardized email content extraction.

-- OCR Engine: Extracts text from attachments.

-- AI Classifier: Zero-shot classification for accurate labeling.

-- FastAPI API: RESTful interface with interactive docs.

### Unique Features

-- Zero-Shot Classification: Classify without training datasets.

-- OCR Fallback: Ensures reliable text extraction.

-- Modular Design: Easily extensible and maintainable.

### Tech Stack & Tools

-- NLP: Hugging Face Transformers

-- OCR: Tesseract

-- API: FastAPI

-- File Handling: PyPDF2, python-docx

### Live Demo & Usage

-- CLI: Single command email processing.

-- API: Interactive Swagger UI for easy testing.

### Impact & Future Work

-- Significant time savings and accuracy improvement.

-- Future: Enhance duplicate detection, integrate advanced NER.

### Thank You & Q&A

Questions?
