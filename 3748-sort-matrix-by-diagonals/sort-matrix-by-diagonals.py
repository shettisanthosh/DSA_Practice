class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        def sortDiagonal(r,c,grid,ascend):
            temp=[]
            i=r;j=c
            while i<n and j<n:
                temp.append(grid[i][j])
                i+=1;j+=1
            if ascend:
                temp.sort()
            else:
                temp.sort(reverse=True)
            i=r;j=c
            for ele in temp:
                grid[i][j]=ele
                i+=1;j+=1
        #bottom triangle
        for r in range(n):
            sortDiagonal(r,0,grid,False)
        #top triangle
        for c in range(1,n):
            sortDiagonal(0,c,grid,True)
        return grid