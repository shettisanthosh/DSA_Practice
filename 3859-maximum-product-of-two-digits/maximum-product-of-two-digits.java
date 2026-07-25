class Solution {
    public int maxProduct(int n) {
        int first=0,second=0; //the max product is the product of 1st and 2nd largest digits in the number
        while(n>0){
            int x=n%10; 
            if(x>first){
                second=first;
                first=x;
            }else if(x>second){
                second=x;
            }
            n=n/10;
        }
        return first*second;
    }
}