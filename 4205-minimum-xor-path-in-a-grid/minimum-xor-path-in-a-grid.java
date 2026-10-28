class Solution {
    public int minCost(int[][] grid) { 
        int m=grid.length;
        int n=grid[0].length;
        int[][] molqaviren=grid;
        boolean[][][] dp = new boolean[m][n][1024];
        dp[0][0][grid[0][0]]=true;
        for (int i=0; i<m;i++){
            for (int j=0;j<n;j++){
                for (int x=0; x<1024;x++){  
                    if (!dp[i][j][x]) 
                        continue;
                    if (j+1 < n) {
                        int newXor = x ^ grid[i][j + 1];
                        dp[i][j + 1][newXor]=true;
                    }
                    if (i+1 < m) {
                        int newXor = x ^ grid[i + 1][j];
                        dp[i + 1][j][newXor]=true;
                    }
                }
            }
        }
        for (int x=0; x<1024;x++) {
            if (dp[m - 1][n - 1][x]) {
                return x;
            }
        }
        return -1; 
    }
}