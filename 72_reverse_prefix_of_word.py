class Solution:
    def reversePrefix(self, word: str, ch: str)-> str:
        stack = []
        index = 0
        if ch not in word:
            return word
        for i in range(len(word)):
            stack.append(word[i])
            if word[i] == ch:
                index = i
                break
        res = ""
        while stack:
            res += stack.pop()
        return res + stack[word + 1:]