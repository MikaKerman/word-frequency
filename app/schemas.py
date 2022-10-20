from pydantic import BaseModel


class WordFrequency(BaseModel):
    word: str
    frequency: int
