from dataclasses import dataclass

@dataclass
class Word:

    id: int
    wordText: str
    langID: int 
    metaData: dict
    