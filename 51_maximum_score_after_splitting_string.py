class Solution:
    def maxScore(self, s: str)-> int:
        one_right = s.count('1')
        zero_left = 0
        max_score = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                zero_left += 1
            else:
                one_right -= 1
            current = zero_left + one_right
            if max_score < current:
                max_score = current
        return max_score