class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        for letter in s:
            if letter in freq1:
                freq1[letter] += 1
            else:
                freq1[letter] = 1

        freq2 = {}
        for letter in t:
            if letter in freq2:
                freq2[letter] += 1
            else:
                freq2[letter] = 1
        
        if freq1 == freq2:
            return True
        return False