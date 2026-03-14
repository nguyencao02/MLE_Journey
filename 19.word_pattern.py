class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        w_to_p={}
        p_to_w ={}
        words = s.split()
        if len(words) != len(pattern):
            return False
        for i in range(len(words)):
            c1 = pattern[i]
            c2 = words[i]
            if c1 in w_to_p:
                if w_to_p[c1] != c2:
                    return False
            if c2 in p_to_w:
                if p_to_w[c2] != c1:
                    return False
            w_to_p[c1] = c2
            p_to_w[c2] = c1
        return True
        