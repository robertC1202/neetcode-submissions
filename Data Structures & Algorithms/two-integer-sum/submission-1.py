class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        freq = {}

        difference = 0

        for i in range(len(nums)):

            difference = target - nums[i]

            if difference in freq:
                return[freq[difference], i]

        
            freq[nums[i]] = i

        
        return []