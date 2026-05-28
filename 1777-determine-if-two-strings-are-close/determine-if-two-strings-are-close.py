from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)

        same_letters = set(word1) == set(word2)
        same_frequencies = sorted(count1.values()) == sorted(count2.values())

        return same_letters and same_frequencies