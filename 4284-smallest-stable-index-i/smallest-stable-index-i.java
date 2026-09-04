class Solution {
    public int firstStableIndex(int[] nums, int k) {
        int mx=Integer.MIN_VALUE;
        int mn=Integer.MAX_VALUE;
        int len=nums.length;
        int help[] = new int[len];
        for(int i=len-1;i>=0;i--){
            mn=Math.min(mn,nums[i]);
            help[i]=mn;
        }
        for(int i=0;i<len;i++){
            mx=Math.max(mx,nums[i]);
            int maxE=mx;
            int minE=help[i];
            if(maxE-minE<=k){
                return i;
            }
        }
        return -1;
    }
}