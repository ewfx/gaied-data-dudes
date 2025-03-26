# src/field_extraction.py

import re

def extract_key_fields(text: str) -> dict:
    """
    Basic example: extract the FIRST $-amount found via regex.
    Potential expansions:
      - advanced NER
      - date extraction
      - deal name, etc.
    """
    # Regex for amounts like $1,234,567.89, 123,456, or 500 USD
    amount_pattern = re.compile(r'(\\$?\\d{1,3}(?:,\\d{3})*(?:\\.?\\d+)?)(\\s?(USD|dollars)?)')
    matches = amount_pattern.findall(text)
    amount = matches[0][0] if matches else None

    return {
        "deal_name": None,
        "amount": amount,
        "expiration_date": None
    }
