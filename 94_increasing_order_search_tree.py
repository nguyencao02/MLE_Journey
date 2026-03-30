class Solution:
    def increasingBST(self, root:Optional[TreeNode])-> Optional[TreeNode]:
        if not root:
            return []
        stack = []
        res = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr)
            curr = curr.right
        dummy = TreeNode[0]
        move = dummy
        for node in res:
            node.left = None
            move.right = node
            move = node
        move.right = None
        return dummy.right
            
            