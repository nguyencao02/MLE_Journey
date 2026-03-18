class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        L = 0
        R = len(nums) - 1
        while L < R:
            if nums[L] % 2 > nums[R] % 2:
                nums[L],nums[R] = nums[R],nums[L]
            if nums[L] % 2 == 0:
                L += 1
            if nums[R] % 2 != 0:
                R -= 1
        return nums