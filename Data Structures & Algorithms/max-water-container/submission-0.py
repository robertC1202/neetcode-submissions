class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxArea = 0
        l, r = 0, len(heights) - 1

        while l < r:

            height = min(heights[l], heights[r])
            width = r - l
            area = height * width

            maxArea = max(maxArea, area)

            if heights[l] > heights[r]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
            else:
                l += 1
        
        return maxArea