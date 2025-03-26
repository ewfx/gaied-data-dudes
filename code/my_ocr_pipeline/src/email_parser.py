# src/email_parser.py

import email

def parse_eml(file_path: str) -> dict:
    """
    Parse .eml file into a dict:
        {
          'subject': ...,
          'from': ...,
          'to': ...,
          'cc': ...,
          'date': ...,
          'body': str,
          'attachments': [ { 'filename': str, 'data': bytes }, ... ]
        }
    """
    with open(file_path, "rb") as f:
        raw_data = f.read()
    msg = email.message_from_bytes(raw_data)

    email_data = {
        "subject": msg.get("subject", ""),
        "from": msg.get("from", ""),
        "to": msg.get("to", ""),
        "cc": msg.get("cc", ""),
        "date": msg.get("date", ""),
        "body": "",
        "attachments": []
    }

    for part in msg.walk():
        filename = part.get_filename()
        ctype = part.get_content_type()

        if filename:  # Attachment
            attach_data = part.get_payload(decode=True)
            email_data["attachments"].append({
                "filename": filename,
                "data": attach_data
            })
        else:
            # Could be text/plain or text/html for body
            if ctype in ["text/plain", "text/html"]:
                try:
                    body_bytes = part.get_payload(decode=True)
                    if body_bytes:
                        email_data["body"] += body_bytes.decode(errors="ignore")
                except:
                    pass

    return email_data
