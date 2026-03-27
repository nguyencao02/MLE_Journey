class Solution:
    def minimumPairRemoval(self, nums: List[int])-> int:
        ans = 0
        while nums != sorted(nums):
            min_val = float('inf')
            min__indx = -1
            for i in range(len(nums) - 1):
                sum = nums[i] + nums[i + 1]
                if sum < min_val:
                    min_val = sum
                    min_indx = i
            nums[min_indx] += nums[min_indx + 1]
            nums.pop(min_indx + 1)
            ans += 1
        return ans