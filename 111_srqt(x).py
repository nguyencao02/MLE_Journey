class Solution:
    def mySqrt(self, x: int)-> int:
        left = 1
        right = x
        while left <= right:
            mid = left + (right - left) // 2
            sqrt = mid * mid
            if sqrt == x:
                return mid
            elif sqrt < x:
                left = mid + 1
            else:
                right = mid - 1                
        return right