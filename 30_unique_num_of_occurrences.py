class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        my_dict = {}
        for num in arr:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1
        count = my_dict.values()
        return len(count) == len(set(count))