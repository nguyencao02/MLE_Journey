class Solution:
    def runningSum(self, nums: list[int]) ->list[int]:
        total = nums[0]
        for i in range (1, len(nums)):
            temp = nums[i]
            nums[i] = temp + total
            total = nums[i]
        return nums