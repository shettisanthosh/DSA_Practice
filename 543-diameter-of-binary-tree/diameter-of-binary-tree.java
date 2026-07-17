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
class Solution {
    private int maxi=-1;
    public int diameterOfBinaryTree(TreeNode root) {
        m_height(root);
        return maxi;
    }
    private int m_height(TreeNode root){
            if(root==null){
                return 0;
            }
            int l=m_height(root.left);
            int r=m_height(root.right);
            maxi=Math.max(maxi,l+r);
            return 1+Math.max(l,r);
    }
    
}