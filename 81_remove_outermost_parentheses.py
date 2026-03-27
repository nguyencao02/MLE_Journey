class Solution:
    def removeOuterParentheses(self, s: str)-> str:
        open = 0
        res = []
        for char in s:
            if char == "(":
                if open > 0:
                    res.append(char)
                open += 1
            else:
                open -= 1
                if open > 0:
                    res.append(char)
        return "". join(res)