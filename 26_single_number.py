class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count_map = {}
        for n in nums:
            if n in count_map:
                count_map[n] += 1
            else:
                count_map[n] = 1
        for n in nums:
            if count_map[n] == 1:
                return n
            