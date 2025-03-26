# scripts/serve_api.py

import os
import tempfile
import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

from src.pipeline import process_email

app = FastAPI(
    title="GenAI Email Classification & OCR API",
    description="A FastAPI service for classifying emails and extracting text/fields from attachments.",
    version="1.0.0",
)

SAMPLE_REQUEST_TYPES = [
    "Adjustments",
    "AU Transfer",
    "Closing Notice",
    "Commitment Change",
    "Fee Payment",
    "Money Movement-Inbound",
    "Money Movement-Outbound"
]

@app.post("/classify_eml")
async def classify_eml(eml_file: UploadFile = File(...)):
    """
    Upload an .eml file to be parsed and classified.
    Returns classification results, extracted fields, etc.
    """
    # Save the uploaded EML to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".eml") as tmp:
        file_path = tmp.name
        content = await eml_file.read()
        tmp.write(content)

    try:
        # Process the file with the pipeline
        result = process_email(file_path, SAMPLE_REQUEST_TYPES)
    except Exception as e:
        # Clean up temp file
        os.remove(file_path)
        return JSONResponse(content={"error": str(e)}, status_code=500)

    # Clean up temp file
    os.remove(file_path)

    return result

if __name__ == "__main__":
    # Run with: python scripts/serve_api.py
    # Then open http://127.0.0.1:8000/docs for Swagger UI
    uvicorn.run(app, host="127.0.0.1", port=8000)
