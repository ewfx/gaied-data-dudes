# scripts/run_pipeline.py

import os
import json

from src.pipeline import process_email

def main():
    # Optionally generate or assume samples are already in test_emails
    # from scripts.generate_samples import generate_sample_emails
    # generate_sample_emails()

    SAMPLE_REQUEST_TYPES = [
        "Adjustments",
        "AU Transfer",
        "Closing Notice",
        "Commitment Change",
        "Fee Payment",
        "Money Movement-Inbound",
        "Money Movement-Outbound"
    ]

    email_dir = "test_emails"
    if not os.path.isdir(email_dir):
        print(f"No {email_dir} directory found. Please provide your .eml files or generate samples.")
        return

    report = []
    for fname in os.listdir(email_dir):
        if fname.lower().endswith(".eml"):
            path = os.path.join(email_dir, fname)
            result = process_email(path, SAMPLE_REQUEST_TYPES)
            report.append(result)

    print("\n===================== Final Report =====================")
    print(json.dumps(report, indent=2))
    print("========================================================")

if __name__ == "__main__":
    main()
