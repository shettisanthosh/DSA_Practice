class Solution {
    public String interpret(String command) {
        String ans="";
        int i=0;
        int l=command.length();
        while(i<l){
            if(command.charAt(i)=='G'){
                ans+="G";
                i++;
            }else if(command.charAt(i)=='(' && command.charAt(i+1)==')'){
                ans+="o";
                i+=2;
            }else{
                ans+="al";
                i+=4;
            }
        }
        return ans;
    }
}