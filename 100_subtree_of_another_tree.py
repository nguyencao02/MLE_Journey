class Solution:
    def issubTree(self, root:Optional[Treenode], subRoot: Optional[TreeNode])-> bool:
        if not root:
            return False
        if self.isSameTree(root,subRoot):
            return True
        return self.issubTree(root.left,subRoot) or self.issubTree(root.right,subRoot)
        
    def isSameTree(self, p, q):
        if not q and not p:
            return True
        if not q or not p or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
