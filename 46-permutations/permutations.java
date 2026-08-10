class Solution {
    List<List<Integer>> l = new ArrayList<>();
    public List<List<Integer>> permute(int[] nums) {
        int n=nums.length;
        boolean check[] = new boolean[n];
        List<Integer> l1 = new ArrayList<>();
        getPermutate(nums,check,l1,n);
        return l;
    }
    public void getPermutate(int nums[], boolean check[],List<Integer>l1,int n){
        if(l1.size()==n){
            l.add(new ArrayList<>(l1));
            return;
        }
        for(int i=0;i<n;i++){
            if(check[i]==false){
                l1.add(nums[i]);
                check[i]=true;
                getPermutate(nums,check,l1,n);
                l1.remove(l1.size()-1);
                check[i]=false;
            }
        }
    }
}