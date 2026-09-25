class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(s) < len(t): 
            return ""
        
        count_T, window_Map = {}, {}

        for c in t:
            count_T[c] = 1 + count_T.get(c, 0)
        
        res = [-1, -1]
        prev_Length = float("infinity")

        have = 0
        required = len(count_T)

        l = 0

        for r in range(len(s)):

            c = s[r]
            window_Map[c] = 1 + window_Map.get(c, 0)

            if c in count_T and window_Map[c] == count_T[c]:
                have += 1
            
            while have == required:

                if (r - l + 1) < prev_Length:

                    res = [l, r]
                    prev_Length = (r - l + 1)
                
                window_Map[s[l]] -= 1

                if s[l] in count_T and window_Map[s[l]] < count_T[s[l]]:
                    have -= 1
                
                l += 1

        l, r = res

        return s[l:r+1] if prev_Length != float("infinity") else ""




