class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for number in nums:
            if number in freq:
                freq[number] += 1
            else:
                freq[number] = 1

        appears = [[] for i in range(len(nums) + 1)]
        for number, count in freq.items():
            appears[count].append(number)

        result = []
        for i in range(len(appears) - 1, 0, -1):
            for number in appears[i]:
                result.append(number)
                if len(result) == k:
                    return result
