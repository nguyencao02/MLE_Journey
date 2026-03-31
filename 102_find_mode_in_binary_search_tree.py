class Solution:
    def findMode(self, root:Optional[TreeNode])-> List[int]:
        self.prev = None
        self.count = 0
        self.maxcount = 0
        self.modes = []
        
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            if self.prev == node.val:
                self.count += 1
            else:
                self.count = 1
            if self.count > self.maxcount:
                self.maxcount = self.count
                self.modes = [node.val]
            elif self.count == self.maxcount:
                self.modes.append(node.val)
            self.prev = node.val
            inorder(node.right)
        inorder(root)
        return self.modes