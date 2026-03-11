class Solution:
    def twoSum(self, nums: List[int], target: int)->List[int]:
        my_dict={}
        for y,x in enumerate(nums):
            n = target - x
            if n in my_dict:
                return [my_dict[n],y]
            else:
                my_dict[x] = y