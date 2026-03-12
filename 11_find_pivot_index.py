class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        to_left = 0
        total = sum(nums)
        for i in range(0, len(nums)):
            temp = nums[i]
            to_right = total - to_left - temp
            if to_left != to_right:
                to_left += temp
            else:
                return i
        return -1