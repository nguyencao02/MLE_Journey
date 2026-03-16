class Solution:
    def firstUniqChar(self, s:str) -> int:
        my_dict = {}
        for indx in s:
            if indx in my_dict:
                my_dict[indx] += 1
            else:
                my_dict[indx] = 1
        for i in range(len(s)):
            if my_dict[s[i]] == 1:
                return i
        return -1