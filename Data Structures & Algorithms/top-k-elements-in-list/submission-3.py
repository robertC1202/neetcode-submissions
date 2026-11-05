class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashMap = {}

        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        
        freq_array = [[] for i in range(len(nums) + 1)]

        for n, c in hashMap.items():
            freq_array[c].append(n)
        
        result = []

        for i in range(len(freq_array) - 1, -1, -1):
            for num in freq_array[i]:
                result.append(num)
                if len(result) == k:
                    return result

        
       

        