class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        my_dict ={}
        for ele, x in enumerate(nums):
            if x in my_dict:
                my_dict[x] += 1
            else:
                my_dict[x] = 1
            if my_dict[x] > len(nums)/2:
                return x