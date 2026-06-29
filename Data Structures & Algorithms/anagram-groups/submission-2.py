class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            arranged = tuple(sorted(word))

            if arranged in groups:
                groups[arranged].append(word)
            else:
                groups[arranged] = [word]

        return list(groups.values())

        