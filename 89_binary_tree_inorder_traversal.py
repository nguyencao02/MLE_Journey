class Solution:
    def preorderTraversal(self, root: Optional[TreeNode])-> List[int]:
        if not root:
            return []
        res = []
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res