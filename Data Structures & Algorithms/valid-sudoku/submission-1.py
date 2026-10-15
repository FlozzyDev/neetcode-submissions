class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):

                # define value
                v = board[r][c]
                if v == ".":
                    continue
                
                b = (r//3) * 3 + (c//3)
                # check if value already exists
                if v in rows[r] or v in cols[c] or v in boxes[b]:
                    return False
                # insert values
                rows[r].add(v)
                cols[c].add(v)
                boxes[b].add(v)
        return True        