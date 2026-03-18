class Solution: 
    def sortedSquares(self,nums: list[int])->list[int]:
        res = [0] * len(nums)
        L = 0
        R = len(nums) - 1
        p = len(nums) - 1
        while L <= R:
            val_L = nums[L]**2
            val_R = nums[R]**2
            if val_L > val_R:
                res[p] = val_L
                L += 1
            else:
                res[p] = val_R
                R -= 1
            p -= 1
        return res