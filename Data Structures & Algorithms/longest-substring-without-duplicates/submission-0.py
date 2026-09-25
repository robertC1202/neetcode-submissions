class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = set()

        l = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in charMap:
                charMap.remove(s[l])
                l += 1
            
            charMap.add(s[r])
            longest = max(longest, r - l + 1)
        
        return longest
            

