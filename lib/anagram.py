# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, candidates):
        """
        Return a list of words from candidates that are anagrams of self.word.
        """
        sorted_word = sorted(self.word)
        return [candidate for candidate in candidates
                if candidate.lower() != self.word
                and sorted(candidate.lower()) == sorted_word]
