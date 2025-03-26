# scripts/generate_samples.py

import os
from typing import List, Tuple

# Example: short base64 for demonstration. Use your actual PDFs if needed.
SCANNED_PDF_BASE64 = b"""
JVBERi0xLjUNCiW1t7IKDQoxIDAgb2JqDTw8IC9DcmVhdG9yIChTY2FubmVkIERvY3Vp
bWVudCBFeGFtcGxlKS9QYWdlcyAyIDAgUi9UeXBlL0NhdGFsb2c+PmVuZG9iajANCjIg
...
"""

ADJUST_PDF_BASE64 = b"""
JVBERi0xLjUNCiW1t7IKDQoxIDAgb2JqDTw8IC9DcmVhdG9yIChUZXh0LVBkZikKL1Bh
Z2VzIDIgMCBSCi9UeXBlL0NhdGFsb2c+PmVuZG9iajANCjIgMCBvYmoNPDwgL0NvdW50
...
"""

def create_eml_file(
    file_path: str,
    subject: str,
    body_text: str,
    attachments: List[Tuple[str, bytes]]
) -> None:
    boundary = "BOUNDARY"
    eml_header = f"""From: testuser@example.com
To: advancedgenai@example.com
Subject: {subject}
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="{boundary}"

"""

    eml_body = (
        f"--{boundary}\n"
        f"Content-Type: text/plain\n\n"
        f"{body_text}\n\n"
    )

    eml_attachments = ""
    for (fname, b64_data) in attachments:
        if fname.lower().endswith(".pdf"):
            content_type = "application/pdf"
        else:
            content_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"

        eml_attachments += (
            f"--{boundary}\n"
            f"Content-Type: {content_type}\n"
            f"Content-Transfer-Encoding: base64\n"
            f"Content-Disposition: attachment; filename=\"{fname}\"\n\n"
            f"{b64_data.decode('utf-8')}\n\n"
        )

    eml_close = f"--{boundary}--\n"

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(eml_header)
        f.write(eml_body)
        f.write(eml_attachments)
        f.write(eml_close)

def generate_sample_emails():
    # 1) EML with scanned PDF referencing Money Movement-Inbound
    inbound_body = (
        "Hello Team,\n\n"
        "We would like to initiate a Money Movement-Inbound transaction for $2,500,000.\n"
        "Attached is a scanned PDF with more info.\n\n"
        "Regards,\nClient SCAN"
    )
    create_eml_file(
        file_path="test_emails/email_inbound_scanned.eml",
        subject="Scanned PDF: Inbound Funding Request",
        body_text=inbound_body,
        attachments=[
            ("scanned_inbound.pdf", SCANNED_PDF_BASE64)
        ]
    )

    # 2) EML referencing Adjustments + text-based PDF
    adjust_body = (
        "Dear Loan Servicing,\n\n"
        "We request an Adjustment for $500, referencing Amendment Fees.\n"
        "Attached is a text-based PDF.\n\n"
        "Thanks,\nAccount Manager"
    )
    create_eml_file(
        file_path="test_emails/email_adjustment_textpdf.eml",
        subject="Adjustment Request - $500 Amendment",
        body_text=adjust_body,
        attachments=[
            ("adjustment_text.pdf", ADJUST_PDF_BASE64)
        ]
    )

    # 3) EML referencing multiple request types in body only
    multi_body = (
        "Hi Team,\n\n"
        "We need a Fee Payment soon. Also, there's an upcoming Money Movement-Inbound.\n"
        "But the Fee Payment is more urgent.\n\n"
        "Regards,\nClient MULTI"
    )
    create_eml_file(
        file_path="test_emails/email_multiple.eml",
        subject="Multiple Requests: Fee & Inbound",
        body_text=multi_body,
        attachments=[]
    )

def main():
    generate_sample_emails()
    print("Sample EML files created in ./test_emails")
    for f in os.listdir("test_emails"):
        if f.endswith(".eml"):
            print(" -", f)

if __name__ == "__main__":
    main()
