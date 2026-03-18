from collections import Counter
class Solution:
    def maxDifference(self, s:str)->int:
        counts = Counter(s)
        all_freqs = counts.value()
        odd_freqs = [v for v in all_freqs if v % 2 != 0]
        even_freqs = [v for v in all_freqs if v % 2 == 0]
        return max(odd_freqs) - min(even_freqs)