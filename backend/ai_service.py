from .config import GEMINI_API_KEY, GEMINI_MODEL

def build_prompt(data):
    return f"""
You are a legal-document drafting assistant.

Create a professional, clearly structured DRAFT legal document.
Do not claim that the document is automatically legally valid. Include a short
"Legal Review Notice" at the end advising review by a qualified legal professional.

Document type: {data.document_type}
Party 1: {data.party_one}
Party 2: {data.party_two}
Effective date: {data.effective_date}
Jurisdiction: {data.jurisdiction}
Main terms and conditions:
{data.terms}

Additional details:
{data.additional_details or "None"}

Use clear headings, numbered clauses, definitions where appropriate,
obligations, confidentiality/termination/payment/dispute provisions when
relevant to the selected document type, and signature sections.
Return plain text suitable for editing and export.
"""

def generate_with_gemini(data):
    if not GEMINI_API_KEY:
        return None

    try:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel(GEMINI_MODEL)
        response = model.generate_content(build_prompt(data))
        text = getattr(response, "text", None)
        return text.strip() if text else None
    except Exception:
        return None

def generate_fallback(data):
    title = data.document_type.upper()
    return f"""DRAFT {title}

LEGAL REVIEW NOTICE
This document is an AI-generated draft for informational and drafting purposes.
It should be reviewed and customized by a qualified legal professional before
being signed or relied upon.

1. PARTIES
Party 1: {data.party_one}
Party 2: {data.party_two}

2. EFFECTIVE DATE
This agreement is intended to take effect on {data.effective_date}.

3. JURISDICTION
This document is intended for use in: {data.jurisdiction}

4. TERMS AND CONDITIONS
{data.terms}

5. ADDITIONAL DETAILS
{data.additional_details or "No additional details were provided."}

6. GENERAL PROVISIONS
The parties should review applicable notices, representations, obligations,
confidentiality, termination, payment, dispute resolution, governing law,
and other provisions appropriate to this document type.

7. SIGNATURES

Party 1 Signature: ______________________________
Name: {data.party_one}
Date: __________________

Party 2 Signature: ______________________________
Name: {data.party_two}
Date: __________________
"""

def generate_document(data):
    ai_text = generate_with_gemini(data)
    return ai_text if ai_text else generate_fallback(data)
