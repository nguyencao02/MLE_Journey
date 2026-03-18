class Solution:
    def countConsistentStrings(self, allowed:str, words: list[str]) -> int:
        count_str = 0
        for word in words:
            is_consistent = True
            for char in word:
                if char not in allowed:
                    is_consistent = False
                    break
            if is_consistent:
                count_str += 1
        return count_str
            
        