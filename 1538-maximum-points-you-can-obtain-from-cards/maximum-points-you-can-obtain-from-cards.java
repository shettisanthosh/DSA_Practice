class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int left=0,right=0,max=0;
        for(int i=0;i<k;i++){
            left+=cardPoints[i];
        }
        max=left;
        int ridx=cardPoints.length-1;
        for(int i=k-1;i>=0;i--){
            left=left-cardPoints[i];
            right=right+cardPoints[ridx];
            ridx--;
            max=Math.max(max,left+right);
        }
        return max;
    }
}