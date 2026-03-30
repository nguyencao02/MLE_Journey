class Solution:
    def preorder(self,root: 'Node')-> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            for child in reversed(curr.children):
                stack.append(child)
        return res
                