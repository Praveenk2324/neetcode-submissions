class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = 0
        count = 0
        for i in range(len(board[0])):
            count += 1
        return count