from app.models import Lead


def enrich_lead(lead: Lead) -> dict:
    handle = lead.name.lower().replace(" ", "")
    return {
        "linkedin_url": f"https://linkedin.com/in/{handle}",
        "company_size": "51-200",
        "industry": "SaaS",
    }


def classify_message(message: str) -> dict:
    text = message.lower()

    if "interested" in text or "buy" in text:
        return {"intent": "sales_enquiry", "confidence": 0.9}

    if "help" in text or "support" in text:
        return {"intent": "support", "confidence": 0.85}

    if "job" in text or "career" in text:
        return {"intent": "job_query", "confidence": 0.8}

    return {"intent": "general", "confidence": 0.6}
