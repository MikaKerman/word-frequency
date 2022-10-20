import logging
from functools import lru_cache
from typing import Optional, List, Dict

from app.schemas import WordFrequency

logger = logging.getLogger(__name__)


class WordsStorage:
    word_count: Dict[str, int]
    _words_frequency: Optional[List[WordFrequency]]

    def __init__(self):
        self.word_count = dict()
        self._words_frequency = None

    @property
    def words_frequency(self) -> List[WordFrequency]:
        if self._words_frequency is None:
            self._calculate_words_frequency()
        return self._words_frequency

    def _add_word(self, word: str) -> None:
        self.word_count.setdefault(word, 0)
        self.word_count[word] += 1

    def _get_least_recurring_word_count(self) -> int:
        return min(self.word_count.values())

    def _get_most_recurring_word_count(self) -> int:
        return max(self.word_count.values())

    @staticmethod
    @lru_cache
    def _calculate_frequency(current_word_count: int, least_occurring_word_count: int,
                             most_occurring_word_count: int) -> int:
        if least_occurring_word_count == most_occurring_word_count:
            return 5
        return round(4 * (current_word_count - least_occurring_word_count) / (
                most_occurring_word_count - least_occurring_word_count)) + 1

    def _calculate_words_frequency(self) -> None:
        if not self.word_count:
            self._words_frequency = []
        else:
            logger.info('Calculating words frequency.')
            words_frequency = list()
            least_recurring_word_count = self._get_least_recurring_word_count()
            most_recurring_word_count = self._get_most_recurring_word_count()

            for word, count in self.word_count.items():
                frequency = self._calculate_frequency(count, least_recurring_word_count, most_recurring_word_count)
                words_frequency.append(WordFrequency(word=word, frequency=frequency))

            self._words_frequency = sorted(words_frequency, key=lambda word_frequency: word_frequency.frequency,
                                           reverse=True)

    def _clear_words_frequency(self) -> None:
        logger.debug('Clearing words frequency.')
        self._words_frequency = None

    def add_words(self, words: List[str]) -> None:
        logger.info('Adding words to the storage.')
        for word in words:
            self._add_word(word)
        self._clear_words_frequency()

    def get_most_recurring_words(self, words_count: int) -> List[WordFrequency]:
        return self.words_frequency[:words_count]
