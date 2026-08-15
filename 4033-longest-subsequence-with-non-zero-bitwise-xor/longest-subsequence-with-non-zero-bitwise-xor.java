class Solution {
    public int longestSubsequence(int[] nums) {
        int n=nums.length;
        boolean zero=true;
        for(int num:nums){
            if(num!=0){
                zero=false;
                break;
            }
        }
        if(zero){
            return 0;
        }
        int x=0;
        for(int num:nums){
            x^=num;
        }
        return x!=0 ? n:n-1;
    }
}