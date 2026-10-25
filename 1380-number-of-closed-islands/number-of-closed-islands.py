class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        count = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0:
                    if self.dfs(grid, i, j):
                        count += 1
        return count
    def dfs(self, grid: list[list[int]], r: int, c: int) -> bool:
        if r < 0 or r >= self.m or c < 0 or c >= self.n:
            return False  # Not closed
        if grid[r][c] == 1:
            return True   # Closed here
        grid[r][c] = 1    # Mark as visited
        # Execute all 4 calls to completely sink/mark the current island
        left = self.dfs(grid, r, c - 1)
        right = self.dfs(grid, r, c + 1)
        up = self.dfs(grid, r - 1, c)
        down = self.dfs(grid, r + 1, c) 
        return left and right and up and down
