# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans=[]
        q=deque()
        q.append(root)
        level=0
        while q:
            size=len(q)
            listt=[]
            for _ in range(size):
                node=q.popleft()
                if node:
                    listt.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level%2==0:
                ans.append(listt)
            else:
                ans.append(listt[::-1])
            level+=1
        return ans