from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Docket:
    docket_id: int
    title: str
    summary: str
    keywords: Optional[List[str]] = None
