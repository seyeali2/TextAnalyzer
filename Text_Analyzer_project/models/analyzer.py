import re

from utils.decorator import validate_text
from utils.exceptions import InvalidPatternError


class TextAnalyzer:

    def __init__(self, text):

        self.text = text

    @validate_text
    def word_count(self):

        words = self.text.split()

        return len(words)

    @validate_text
    def most_common_words(self):

        words = self.text.lower().split()

        frequencies = {}

        for word in words:

            frequencies[word] = frequencies.get(word, 0) + 1

        sorted_words = sorted(
            frequencies.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return sorted_words

    @validate_text
    def search_pattern(self, pattern):

        try:

            return re.findall(
                pattern,
                self.text
            )

        except re.error:

            raise InvalidPatternError(
                pattern
            )

    def words_generator(self):

        for word in self.text.split():

            yield word

    def long_words(self):

        return [
            word
            for word in self.text.split()
            if len(word) > 4
        ]