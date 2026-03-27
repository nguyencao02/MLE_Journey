class Solution:
    def findMissingAndRepeatedValues(self, grid: List[int])-> List[int]:
        n = len(grid)
        limit = n * n
        counts = [0]*(limit + 1)
        for row in grid:
            for num in row:
                counts[num] += 1
        a = -1
        b = -1
        for i in range(1, limit + 1):
            if counts[i] == 2:
                a = i
            elif counts[i] == 0:
                b = i
        return [a,b]