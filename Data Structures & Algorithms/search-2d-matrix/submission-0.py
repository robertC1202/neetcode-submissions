class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        size_of_matrix = m * n

        l = 0
        r = size_of_matrix - 1

        while l <= r:
            mid_point = (l+r) //2
            row = mid_point // n
            column = mid_point % n

            desired_number = matrix[row][column]

            if desired_number == target:
                return True
            elif desired_number > target:
                r = mid_point - 1
            else:
                l = mid_point + 1
        
        return False