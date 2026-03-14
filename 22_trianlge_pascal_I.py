class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        for i in range (1,numRows):
            pre_row = res[-1]
            new_row = [1]*(i+1)
            for j in range (1,i):
                new_row[j] = pre_row[j-1] + pre_row[j]
            res.append(new_row)
        return res