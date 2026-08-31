/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        if(head==null || head.next==null || head.next.next==null){
            return new int[]{-1,-1};
        }
        int first=-1;
        int prev=-1;
        int minD=Integer.MAX_VALUE;
        ListNode prevN=head;
        ListNode currN=head.next;
        int i=1;
        while(currN.next!=null){
            ListNode nextN=currN.next;
            boolean isMax=currN.val > prevN.val && currN.val >nextN.val;
            boolean isMin=currN.val<prevN.val && currN.val<nextN.val;
            if(isMax || isMin){
                if(first==-1){
                    first=i;
                }else{
                    minD=Math.min(minD,i-prev);
                }
                prev=i;
            }
            prevN=currN;
            currN=nextN;
            i++;
        }
        if(first==prev){
            return new int[]{-1,-1};
        }
        return new int[]{minD,prev-first};
    }
}