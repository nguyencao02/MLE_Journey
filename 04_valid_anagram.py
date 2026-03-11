class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        if len(t) != len(s):
            return False
        mys_dict ={}
        myt_dict ={}
        
        for slet in s:
            if slet in mys_dict:
                mys_dict[slet] += 1
            else:
                mys_dict[slet] = 1
        for tlet in t:
            if tlet in myt_dict:
                myt_dict[tlet] += 1
            else:
                myt_dict[tlet] = 1
        return mys_dict == myt_dict