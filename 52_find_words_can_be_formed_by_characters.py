from collections import Counter
class Solution:
    def countCharacters(self, words: list[str], chars: str) ->int:
        countchar = Counter(chars)
        total = 0
        for word in words:
            countword = Counter(word)
            can_form = True
            for char in countword:
                if countword[char] > countchar[char]:
                    can_form = False
                    break
            if can_form:
                total += len(word)
        return total
            