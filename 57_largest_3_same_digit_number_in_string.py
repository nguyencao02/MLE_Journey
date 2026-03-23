class Solution:
    def largestGoodInteger(self, num: str)-> str:
        max_digit = -1
        for i in range (len(num)-2):
            if num[i] == num [i + 1] == num [i + 2]:
                max_digit = max(max_digit, int(num[i]))
        if max_digit == -1 :
                return ""
        return str(max_digit)*3
            