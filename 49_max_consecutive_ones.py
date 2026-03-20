class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int])-> int:
        current = 0
        max_count = 0
        for num in nums:
            if num == 1:
                current += 1
                if max_count < current:
                    max_count = current
            else:
                current = 0
        return max_count