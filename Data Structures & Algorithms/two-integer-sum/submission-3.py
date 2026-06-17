class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}
        for index, value in enumerate(nums):
            pair[value] = index

        for i in range(len(nums)):
            goal = target - nums[i]
            if goal in pair and pair[goal] != i:
                return [i, pair[goal]]

        return []