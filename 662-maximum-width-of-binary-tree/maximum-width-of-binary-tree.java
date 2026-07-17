/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
 class Pair{
    TreeNode node;
    int index;
    Pair(TreeNode node,int index){
        this.index=index;
        this.node=node;
    }
 }
class Solution {
    public int widthOfBinaryTree(TreeNode root) {
        if(root==null){
            return 0;
        }
        Queue<Pair> queue = new LinkedList<>();
        queue.offer(new Pair(root,0));
        int maxwidth=0;
        while(!queue.isEmpty()){
            int size=queue.size();
            int minidx=queue.peek().index;
            int first=0;
            int last=0;
            for(int i=0;i<size;i++){
                Pair current = queue.poll();
                int curridx=current.index-minidx;
                if(i==0){
                    first=curridx;
                }
                if(i==size-1){
                    last=curridx;
                }
                if(current.node.left!=null){
                    queue.offer(new Pair(current.node.left,2*curridx+1));
                }
                if(current.node.right!=null){
                    queue.offer(new Pair(current.node.right,2*curridx+2));
                }
            }
            maxwidth=Math.max(maxwidth,last-first+1);
        }
        return maxwidth;
    }
}