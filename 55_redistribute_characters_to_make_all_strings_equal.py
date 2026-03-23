from collections import Counter
class Solution:
    def makeEqual(self,words: List[int])->bool:
        count = Counter("".join(words))
        n = len(words)
        for char in count:
            if count[char] % n != 0:
                return False
        return True