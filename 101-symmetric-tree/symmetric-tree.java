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
// Approach 1 normally done by using recursion
class Solution {
    public boolean isSymmetric(TreeNode root) {
        if(root==null){
            return true;
        }
        return mirror(root.left,root.right);
    }
    boolean mirror(TreeNode l, TreeNode r){
        if(l==null && r==null){
            return true;
        }
        if(l==null || r==null){
            return false;
        }
        if(l.val!=r.val){
            return false;
        }
        return mirror(l.left,r.right) && mirror(l.right,r.left);
    }
}
// Approach 2 solved using Iterative way using 2 Queues basically Level Order Traversal
class Solution {
    public boolean isSymmetric(TreeNode root) {
         if(root==null){
            return true;
        }
        Queue<TreeNode>leftTree= new LinkedList<>();
        Queue<TreeNode>rightTree= new LinkedList<>();
        leftTree.offer(root.left);
        rightTree.offer(root.right);
        while(!leftTree.isEmpty() && !rightTree.isEmpty()){
            TreeNode leftNode=leftTree.poll();
            TreeNode rightNode = rightTree.poll();
            if(leftNode==null && rightNode==null){
                continue;
            }
             if(leftNode==null || rightNode==null){
                return false;
            }
            if(leftNode.val!=rightNode.val){
                return false;
            }
            leftTree.offer(leftNode.left);
            leftTree.offer(leftNode.right);
            rightTree.offer(rightNode.right);
            rightTree.offer(rightNode.left);
        }
        return true;
    }
}
