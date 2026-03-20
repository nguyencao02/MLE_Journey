class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int)-> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_side = (i == 0) or (flowerbed[i - 1] == 0)
                right_side = (i == len(flowerbed) - 1) or (flowerbed[i+1] == 0)
                if left_side and right_side:
                    flowerbed[i] = 1
                    n -= 1
        return n <= 0
    
                