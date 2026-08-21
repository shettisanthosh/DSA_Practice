class Solution {
    public int answer(int idx, int curOr, int[] nums,int maxOr){
        if(idx==nums.length){
            if(curOr==maxOr){
                return 1;
            }
            return 0;
        }
        int consider = answer(idx+1,curOr|nums[idx],nums,maxOr);
        int noConsider = answer(idx+1,curOr,nums,maxOr);
        return consider+noConsider;
    }
    public int countMaxOrSubsets(int[] nums) {
        int maxOr=0;
        for(int num:nums){
            maxOr|=num;
        }
        int curOr=0;
        return answer(0,curOr,nums,maxOr);
    }
}