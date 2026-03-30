class Solution:
    def postorderTraversal(self, root: Optional([TreeNode]))-> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            curr = stack.pop()
            res.append(curr)
            if curr.left:
                res.append(curr.left)
            if curr.right:
                res.append(curr.right)
        return res[::-1]