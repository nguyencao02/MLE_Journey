class Solution:
    def maxDepth(self, root: Optional[TreeNode])-> int:
        if not root:
            return 0
        leftside = self.maxDepth(root.left)
        rightside = self.maxDepth(root.right)
        total = 1 + max(leftside,rightside)
        return total