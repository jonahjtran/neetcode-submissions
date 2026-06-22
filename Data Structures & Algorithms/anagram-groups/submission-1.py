import numpy as np
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            frequency = [0] * 26
            for letter in word:
                frequency[ord(letter) - ord('a')] += 1

            key = tuple(frequency)
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]

        return list(anagrams.values())
