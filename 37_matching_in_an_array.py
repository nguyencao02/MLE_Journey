class Solution:
    def stringMatching (self, words: list[str])->list[str]:
        res = []
        for word in words:
            for other in words:
                if word != other and word in other:
                    res.append(word)
                    break
        return res
        