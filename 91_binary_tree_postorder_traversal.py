class Solution:
    def postorderTraversal(self, root: Optional([TreeNode]))-> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return res[::-1]