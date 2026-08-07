class Solution {
    public String decodeMessage(String key, String message) {
        HashMap<Character,Character> hm = new HashMap<>();
        char alpha='a';
        for(char ch:key.toCharArray()){
            if(ch==' ' || hm.containsKey(ch)){
                continue;
            }
            hm.put(ch,alpha);
            alpha++;
        }
        String str="";
        for(char ch:message.toCharArray()){
            if(ch!=' '){
                str+=hm.get(ch);
            }else{
                str+=' ';
            }
        }
        return str;
    }
}