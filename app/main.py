import logging
from typing import List

from fastapi import FastAPI

from app.schemas import WordFrequency
from app.words_storage import WordsStorage

words_storage = WordsStorage()
app = FastAPI()


@app.post('/words/', description='Add new words to the storage.')
async def post_words(words: List[str]) -> None:
    words_storage.add_words(words)


@app.get('/word_frequency/', description='Get the 5 most recurring words with their frequency distribution rank.')
async def read_word_frequency() -> List[WordFrequency]:
    return words_storage.get_most_recurring_words(words_count=5)


if __name__ == "__main__":
    # for debugging purposes only
    import uvicorn

    logging.basicConfig(level=logging.DEBUG)
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
