"""This module serves as the entry point for the backend of the regulations-llm application."""

from src.backend.ingestion.docket_extraction_service import DocketExtractionService
from src.backend.keywords.local_nlp_keyword_service import LocalNLPKeywordService

def backend():
    """This gets the dockets from the data and extracts the keywords."""
    
    # Get the dat
    print("Starting docket extraction and keyword extraction process...")
    docket_extraction_service = DocketExtractionService()
    dockets = docket_extraction_service.load_dockets_from_json("temp-data/dockets.json")
    print("Loaded dockets:", dockets)
    
    # Get some keywords
    local_nlp_keyword_service = LocalNLPKeywordService()
    local_nlp_keyword_service.extract_keywords(dockets)
    print(dockets)

    # Get some themes from the keywords

    # 
