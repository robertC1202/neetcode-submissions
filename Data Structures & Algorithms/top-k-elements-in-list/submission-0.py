class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequencyBucket = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, cnt in count.items():
            frequencyBucket[cnt].append(num)
        
        result = []

        for i in range(len(frequencyBucket)-1, 0, -1):
            for num in frequencyBucket[i]:
                result.append(num)
                if len(result) == k:
                    return result

        
