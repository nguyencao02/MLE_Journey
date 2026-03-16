class Solution:
    def reverseVowels(self, s:str)-> str:
        s = list(s)
        vowels = set("aeiouAEIOU")
        L = 0
        R = len(s) - 1
        while L < R:
            if s[L] not in vowels:
                L += 1
            elif s[R] not in vowels:
                R -= 1
            else:
                s[L],s[R]=s[R],s[L]
                L += 1
                R -= 1
        return "".join(s)