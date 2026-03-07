from dataclasses import dataclass
from uuid import UUID

@dataclass
class Page:
    id: UUID
    url: str
    title: str
    contents: str
    links: set[str]


