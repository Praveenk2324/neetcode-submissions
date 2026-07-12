class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = 0
        def check(boardorder):
            seen = set()
            duplicate = []
            for i in boardorder:
                if i in seen:
                    duplicate.append(i)
                else:
                    seen.add(i)
            if seen:
                return True
            else:
                return False
        
        horz = check(board[0])
        vert = check(board[1])
        if horz and vert:
            return True
        else:
            return False






