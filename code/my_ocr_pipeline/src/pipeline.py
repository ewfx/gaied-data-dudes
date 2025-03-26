# src/pipeline.py

import os
from typing import List

from src.email_parser import parse_eml
from src.attachment_extractor import extract_text_from_attachments
from src.classification import classify_request_types
from src.domain_rules import apply_domain_rules
from src.field_extraction import extract_key_fields
from src.duplicate_check import check_duplicate

def process_email(file_path: str, request_types: List[str]) -> dict:
    """
    End-to-end pipeline for a local EML file:
      1) Parse EML
      2) Extract text from attachments (with OCR fallback)
      3) Classify request types
      4) Apply domain rules
      5) Extract key fields
      6) Check duplicates
    """
    eml_data = parse_eml(file_path)
    body_text = eml_data["body"]

    attachments_text = extract_text_from_attachments(eml_data["attachments"])
    combined_text = body_text + "\n" + attachments_text

    scores = classify_request_types(combined_text, request_types)
    primary_request, sub_requests = apply_domain_rules(scores)

    extracted_fields = extract_key_fields(combined_text)
    duplicate_flag, duplicate_reason = check_duplicate(eml_data, combined_text)

    if not primary_request:
        primary_request = "Unknown"

    return {
        "filename": os.path.basename(file_path),
        "primary_request_type": {
            "label": primary_request,
            "confidence": scores.get(primary_request, 0.0),
            "reasoning": f"Detected {primary_request} with domain rules."
        },
        "sub_request_types": [
            {
                "label": sr,
                "confidence": scores.get(sr, 0.0)
            } for sr in sub_requests
        ],
        "extracted_fields": extracted_fields,
        "duplicate_flag": duplicate_flag,
        "duplicate_reason": duplicate_reason
    }
