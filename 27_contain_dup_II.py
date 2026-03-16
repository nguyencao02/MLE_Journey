class Solution:
    def containsnearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}
        for indx, val in enumerate(nums):
            if val in seen:
                if indx - seen[val] <= k:
                    return True
            seen[val] = indx
        return False