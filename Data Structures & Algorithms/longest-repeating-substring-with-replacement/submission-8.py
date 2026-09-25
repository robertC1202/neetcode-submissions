class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        countArray = [0] * 26
        l = 0
        longest = 0

        for r in range(len(s)):

            countArray[ord(s[r]) - ord('A')] += 1

            while (r-l+1) - max(countArray) > k:

                countArray[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            longest = max(longest, (r-l+1))

        return longest       
        
