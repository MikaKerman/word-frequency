from app.schemas import WordFrequency
from app.words_storage import WordsStorage


def test_storage_frequency():
    words = ['ball', 'ball', 'ball', 'ball', 'eggs', 'eggs', 'pool', 'pool', 'wild', 'daily']
    words_storage = WordsStorage()
    words_storage.add_words(words)
    assert words_storage.words_frequency == [
        WordFrequency(word='ball', frequency=5), WordFrequency(word='eggs', frequency=2),
        WordFrequency(word='pool', frequency=2), WordFrequency(word='wild', frequency=1),
        WordFrequency(word='daily', frequency=1)]


def test_empty_storage():
    words_storage = WordsStorage()
    assert words_storage.words_frequency == []


def test_storage_with_one_word():
    words = ['home', 'home', 'home']
    words_storage = WordsStorage()
    words_storage.add_words(words)
    assert words_storage.words_frequency == [WordFrequency(word='home', frequency=5)]


def test_same_amount_of_words():
    words = ['home', 'home', 'home', 'daily', 'daily', 'daily', 'pool', 'pool', 'pool']
    words_storage = WordsStorage()
    words_storage.add_words(words)
    assert all([word_frequency.frequency == 5 for word_frequency in words_storage.words_frequency])
