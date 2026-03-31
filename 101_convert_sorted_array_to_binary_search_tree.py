class Solution:
    def sortedArrayToBST(self, nums: List[int])->Optional[TreeNode]:
        def buildtree(left_idx,right_idx):
            if left_idx > right_idx:
                return None
            mid = (left_idx + right_idx) // 2
            root = TreeNode(nums[mid])
            root.left = buildtree(left_idx, mid - 1)
            root.right = buildtree(mid + 1, right_idx)
            return root
        return buildtree(0,len(nums)-1)