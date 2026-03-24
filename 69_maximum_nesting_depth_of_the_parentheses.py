class Solution:
    def maxDepth(self, s: str)-> int:
        stack = []
        max_d = 0
        for char in s:
            if char == "(":
                stack.append("(")
                max_d = max(max_d,len(stack))
            elif char == ")":
                stack.pop()
        return max_d