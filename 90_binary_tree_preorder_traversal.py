class Solution:
    def preorderTraversal(self, root: Optional[TreeNode])-> List[int]:
        if not root:
            return[]
        stack = [root]
        res = []
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right:
                res.append(curr.right)
            if curr.left:
                res.append(curr.left)
        return res