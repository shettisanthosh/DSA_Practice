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
        int count=0;
        ListNode temp=head;
        while(temp!=null){
            count++;
            temp=temp.next;
        }
        int arr[]=new int[count];
        temp=head;
        int index=0;
        while(temp!=null){
            arr[index]=temp.val;
            index++;
            temp=temp.next;
        }
        ArrayList<Integer> criticalPoints = new ArrayList<>();
        for (int i = 1; i < count - 1; i++) {
            boolean isLocalMaxima = arr[i] > arr[i - 1] && arr[i] > arr[i + 1];
            boolean isLocalMinima = arr[i] < arr[i - 1] && arr[i] < arr[i + 1];
            if (isLocalMaxima || isLocalMinima) {
                criticalPoints.add(i + 1); 
            }
        }
        if (criticalPoints.size() < 2) {
            return new int[]{-1, -1};
        }
        int minDistance = Integer.MAX_VALUE;
        int maxDistance = criticalPoints.get(criticalPoints.size() - 1) - criticalPoints.get(0);
        for (int i = 1; i < criticalPoints.size(); i++) {
            int currentDistance = criticalPoints.get(i) - criticalPoints.get(i - 1);
            minDistance = Math.min(minDistance, currentDistance);
        }
        return new int[]{minDistance, maxDistance};
    }
}