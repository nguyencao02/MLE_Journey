class Solution:
    def isUnivalTree(self, root: Optional[TreeNode])-> bool:
        if not root:
            return True
        def check (node,val):
            if not node:
                return True
            if node.val != val:
                return False
            return check(node.left,val) and check (node.right,val)
        return (root,root.val)