# Bitasmbl-File-Converter-PDF-Text-Image-PNG-9386af-

## Description
Build a web application that allows users to upload files and convert them between formats, such as PDF to text or images to PNG. The system focuses on simplicity, intuitive UI, and fast conversions without requiring complex setup.

## Tech Stack
- FastAPI
- React
- Tailwind CSS

## Requirements
- Allow users to upload PDF and image files
- Convert PDF documents to text and images to PNG format
- Provide download links for converted files
- Show status updates during conversion (loading/progress)
- Handle unsupported file types and errors gracefully

## Installation
bash
git clone https://github.com/MrBitasmblTester2/Bitasmbl-File-Converter-PDF-Text-Image-PNG-9386af-.git
cd Bitasmbl-File-Converter-PDF-Text-Image-PNG-9386af-
# backend
pip install fastapi
# frontend
npm install


## Usage
bash
# backend
uvicorn main:app
# frontend
npm start


## Implementation Steps
1. Set up FastAPI server and static file handling.
2. Implement file upload endpoints for PDF and images.
3. Add PDF-to-text conversion logic.
4. Add image-to-PNG conversion logic.
5. Create React UI for uploads, status, and downloads.
6. Integrate Tailwind CSS for styling.
7. Add error handling for unsupported types and failures.

## API Endpoints
- POST /upload/pdf
- POST /upload/image
- GET /download/{file_id}