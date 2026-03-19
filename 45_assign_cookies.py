class Solution:
    def findContentChildren(self, g: list[int], s: list[int])-> int:
        s.sort()
        g.sort()
        childi = 0
        cookiesj = 0
        while childi < len(g) and cookiesj < len(s):
            if s[cookiesj] >= g[childi]:
                childi += 1
            cookiesj += 1
        return childi
        