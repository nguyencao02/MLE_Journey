class Solution:
    def mySqrt(self,x : int)-> int:
        if x == 0 or x == 1:
            return x
        left = 1
        right = x
        while left <= right:
            mid = left + (right - left) // 2
            sqrtnum = mid * mid
            if sqrtnum < x:
                left = mid + 1
            elif sqrtnum > x:
                right = mid - 1
            else:
                return mid
        return right