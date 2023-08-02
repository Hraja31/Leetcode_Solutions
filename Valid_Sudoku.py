class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        arr=[]
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if(val !="."):
                    arr+=[(val,i),(j,val),(i//3,j//3,val)]
        if(len(arr)==len(set(arr))):
            return True
        return False
