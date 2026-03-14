class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_to_t = {}
        map_t_to_s = {}
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            if c1 in map_s_to_t:
                if map_s_to_t[c1] != c2:
                    return False
            if c2 in map_t_to_s:
                if map_t_to_s[c2] != c1:
                    return False
            map_s_to_t[c1] = c2
            map_t_to_s[c2] = c1
        return True
            