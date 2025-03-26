# src/classification.py

from typing import List, Dict
from transformers import pipeline

# Instantiate the pipeline once at import time for reusability
classifier = pipeline("zero-shot-classification", model="roberta-large-mnli")

def classify_request_types(text: str, candidate_labels: List[str]) -> Dict[str, float]:
    """
    Use roberta-large-mnli zero-shot classification to get probabilities for each candidate label.
    """
    if not text.strip():
        return {lbl: 0.0 for lbl in candidate_labels}

    # multi_label=True => it will consider each label independently
    result = classifier(text, candidate_labels, multi_label=True)
    scores_dict = {}
    for label, score in zip(result["labels"], result["scores"]):
        scores_dict[label] = score

    return scores_dict
