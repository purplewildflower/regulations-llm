from src.backend.ingestion.docket_extraction_service import DocketExtractionService
from src.backend.keywords.keyword_extraction_service import KeywordExtractionService

def backend():
    print("Starting docket extraction and keyword extraction process...")
    docket_extraction_service = DocketExtractionService()
    dockets = docket_extraction_service.load_dockets_from_json("../../temp-data/dockets.json")
    print("Loaded dockets:", dockets)
    keyword_service = KeywordExtractionService()
    keyword_service.extract_keywords(dockets)
    print(dockets)
