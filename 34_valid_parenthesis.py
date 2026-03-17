class Solution:
    def isValid(self,s:str)->bool:
        validprts = {"{":"}","[":"]","(":")"}
        stack = []
        for char in s:
            if char in validprts:
                stack.append(char)
            else:
                if not stack:
                    return False
                near_closed = stack.pop()
                if validprts[near_closed] != char:
                    return False
        return len(stack) == 0       