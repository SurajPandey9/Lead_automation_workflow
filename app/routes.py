from fastapi import APIRouter

from app.models import Lead, Message
from app.services import classify_message, enrich_lead

router = APIRouter()


@router.get("/", tags=["Health"])
def home() -> dict:
    return {"message": "API is working"}


@router.post("/enrich", tags=["Lead Enrichment"])
def enrich(lead: Lead) -> dict:
    return enrich_lead(lead)


@router.post("/classify", tags=["Intent Classification"])
def classify(msg: Message) -> dict:
    return classify_message(msg.message)
