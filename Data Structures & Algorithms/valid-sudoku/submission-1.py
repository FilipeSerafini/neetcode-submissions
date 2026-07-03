class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        hm = {}
        for row in board:
            hm = {}
            for num in row:
                if num == ".":
                    continue
                if num in hm:
                    return False
                hm[num] = num

        # check columns
        for col in range(9):
            hm = {}
            for r in range(9):
                num = board[r][col]
                if num == ".":
                    continue
                if num in hm:
                    return False
                hm[num] = num


        box_maps = [{}, {}, {}]
        for row in range(9):
            if row % 3 == 0:
                box_maps = [{}, {}, {}]

            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue

                box_idx = col // 3
                if num in box_maps[box_idx]:
                    return False
                box_maps[box_idx][num] = num

        # boxHm = {}
        # startHor = 0
        # for i in range(9):
        #     for j in range(startHor, 9):
        #         curr = board[i][j]
        #         if curr == ".":
        #             continue
        #         if curr in boxHm:
        #             return False

        #         boxHm[curr] = curr
                
        #         if (j+1) % 3 == 0:
        #             break
            
        #     if (i+1) % 3 == 0:
        #         boxHm = {}

        #     if i == 8:
        #         i = 0
        #         startHor = 3
        return True


