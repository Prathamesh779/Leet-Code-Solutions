class Solution(object):
    def isValidSudoku(self, board):
        rows = set()
        cols = set()
        boxes = set()

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                if (r, num) in rows:
                    return False
                if (c, num) in cols:
                    return False
                if ((r // 3, c // 3), num) in boxes:
                    return False

                rows.add((r, num))
                cols.add((c, num))
                boxes.add(((r // 3, c // 3), num))

        return True