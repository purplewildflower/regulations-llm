from typing import List
from src.backend.models.docket import Docket

class KeywordExtractionService:
    def extract_keywords(self, dockets: List[Docket]) -> None:
        """
        Extracts keywords from each docket's title and summary and sets them in the docket's keywords field.
        Modifies the dockets in place and returns None.
        """
        import re
        for docket in dockets:
            text = f"{docket.title} {docket.summary}"
            # Simple keyword extraction: split by non-word characters, filter short words
            words = re.findall(r'\b\w{4,}\b', text.lower())
            docket.keywords = list(set(words))
