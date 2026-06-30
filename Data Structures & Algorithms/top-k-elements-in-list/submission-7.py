class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # key: number: value: frequency
        freq1 = {}
        for num in nums:
            if num in freq1:
                freq1[num] += 1
            else:
                freq1[num] = 1

        print(freq1)


        # key: frequency, value: number
        freq2 = [[] for i in range(len(nums)+1)]
        for num, count in freq1.items():
            freq2[count].append(num)

        print(freq2)

        result = []
        for i in range(len(freq2)-1,0,-1):
            group = freq2[i]
            print(group)
            for number in group:
                result.append(number)
                if len(result) == k:
                    return result

        return result
            

        

        