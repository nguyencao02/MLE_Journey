class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode])-> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return 0
            tole = dfs(node.left)
            tori = dfs(node.right)
            self.ans = max(self.ans,tole+tori)
            return max(tole,tori) + 1
        dfs(root)
        return self.ans
    
        