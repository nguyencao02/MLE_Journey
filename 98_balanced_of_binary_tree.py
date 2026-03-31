class Solution:
    def isBalanced(self, root: Optional[TreeNode])-> bool:
        def check(node):
            if not node:
                return 0
            leftside = check(node.left)
            if leftside == -1:
                return -1
            rightside = check(node.right)
            if rightside == -1:
                return -1
            if abs(leftside - rightside) > 1:
                return -1
            return max(leftside,rightside) + 1
        return check(root) != -1