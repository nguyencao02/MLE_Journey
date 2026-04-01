class Solution:
    def getMinimumDifference(self,root: Optional[TreeNode])-> int:
        self.prev = None
        self.min_dist = float('inf')
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            if self.prev is not None:
                self.min_dist = min(self.min_dist,node.val - self.prev)
            self.prev = node.val
            inorder(node.right)
        inorder(root)
        return self.min_dist
        
        