class Solution:
    def findtheDifference(self, s: str, t:str) ->str:
        my_dict = {}
        for char in s:
            my_dict[char] = my_dict.get(char, 0) + 1
        for char in t:
            if char not in my_dict or my_dict[char]:
                return char
            my_dict[char] -= 1