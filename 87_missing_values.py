class Solution:
    def missingNumber(self, nums: List[int])-> int:
        n = len(nums)
        limit = n * 1
        counts = [0]*(limit+1)
        for num in nums:
            counts[num] += 1
        a = -1
        for i in range(limit+1):
            if counts[num] == 0:
                a = i
        return a