class Solution:
    def numsDisappeard (self, nums: list[int]) -> list[int]:
        res = []
        for x in nums:
            val = abs(x)
            index = val - 1
            if nums[index] > 0:
                nums[index] = - nums[index]
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res