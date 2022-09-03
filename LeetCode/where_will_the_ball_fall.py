class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        tot = len(grid[0])
        arr = []
        rows = len(grid)
        for i in range(tot):
            col = i
            j = 0
            while True:
                if grid[j][col] == -1:
                        # if same row and col - is 
                    check = -1
                else:
                    check = 1 
                if col<tot and col+check < tot and col+check >-1 and grid[j][col] == grid[j][col + check]:
                    ### check if the previous or latter according to the sign - same or not
                    # increase row count no matter what
                    
                    j += 1   
                    # increase column based on the next check 
                    if j == rows:
                        ans = col + check 
                        arr.append(ans)
                        break
                        
                    if check == -1:
                        col -= 1
                    else:
                        col += 1
                else:
                    arr.append(-1)
                    break
        return arr