class Solution:
    def backspaceCompare(self, s: str, t: str)-> bool:
        def build_String(input_str):
            stack = []
            for char in input_str:
                if char != "#":
                    stack.append(char)
                elif stack:
                    stack.pop()
            return "".join(stack)
        return build_String(s) == build_String(t)
                    
