class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        rows = [0] * 9
        columns = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue
                
                value = int(board[r][c]) - 1

                if (1 << value) & rows[r]:
                    return False
                
                if (1 << value) & columns[c]:
                    return False
                
                if (1 << value) & squares[(r//3) * 3 + (c//3)]:
                    return False
                
                rows[r] |= (1 << value)
                columns[c] |= (1 << value)
                squares[(r//3) * 3 + (c//3)] |= (1 << value)
        
        return True