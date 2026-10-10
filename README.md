# LegalEase

LegalEase is a Generative-AI-powered legal document drafting platform.

## Technology

- Frontend: HTML, CSS, JavaScript
- Backend: Python + FastAPI
- AI: Google Gemini API
- Exports: PDF, DOCX, TXT
- Configuration: `.env`

## Project Structure

```text
LegalEase/
├── backend/
│   ├── main.py
│   ├── ai_service.py
│   ├── document_generator.py
│   ├── models.py
│   └── config.py
├── frontend/
│   ├── index.html
│   ├── css/style.css
│   └── js/app.js
├── generated_documents/
├── .env.example
├── requirements.txt
├── run.bat
└── README.md
```

## Setup on Windows

Open PowerShell in the LegalEase folder.

### 1. Check Python

```powershell
py --version
```

Python 3.8 or newer is recommended.

### 2. Create virtual environment

```powershell
py -m venv venv
```

### 3. Activate

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again.

### 4. Install packages

```powershell
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
```

### 5. Configure Gemini

Copy `.env.example` to `.env`:

```powershell
copy .env.example .env
```

Open `.env` and replace:

```text
YOUR_GEMINI_API_KEY_HERE
```

with your Google Gemini API key.

### 6. Start the application

```powershell
py -m uvicorn backend.main:app --host 127.0.0.1 --port 8000
```

Open:

```text
http://127.0.0.1:8000
```

## Without an API key

The application also contains a local fallback draft generator. This lets you test the frontend, backend, and export functions without an API key. For actual AI-generated drafting, configure the Gemini API key.

## Important

LegalEase produces AI-generated document drafts. It is not a substitute for legal advice. Important documents should be reviewed by a qualified legal professional before signing or relying on them.

## Note about Gemini model availability

The project uses the requested `gemini-1.5-pro` setting by default. Google AI model availability can change over time. If that model is unavailable for your API account, update `GEMINI_MODEL` in `.env` to a currently supported model available to your account.
