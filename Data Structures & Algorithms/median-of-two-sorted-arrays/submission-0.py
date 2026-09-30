class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A
        
        l = 0
        r = len(A) - 1

        while True:
            mid_A = (l+r) // 2
            mid_B = half - (mid_A + 1) - 1

            Aleft = A[mid_A] if mid_A >= 0 else float("-infinity")
            Aright = A[mid_A + 1] if (mid_A + 1) < len(A) else float("infinity")
            Bleft = B[mid_B] if mid_B >= 0 else float("-infinity")
            Bright = B[mid_B + 1] if (mid_B + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:

                #Odd case
                if total % 2 == 1:
                    return min(Aright, Bright)
                
                #even case
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright:
                r = mid_A - 1
            else:
                l = mid_A + 1
        
