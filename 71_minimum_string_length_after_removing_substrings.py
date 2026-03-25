class Solution:
    def minLength(self, s: str)-> int:
        stack = []
        for char in s:
            if stack:
                if (stack[-1] == "A" and char == "B") or (stack[-1] == "C" or char == "D"):
                    stack.pop()
                    continue
            stack.append(char)
        return len(stack)
        
            