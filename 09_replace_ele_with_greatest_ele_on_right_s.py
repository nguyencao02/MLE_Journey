class Solution:
    def replaceElements(self, arr: list[int]) ->list[int]:
        currmax = -1
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = currmax
            currmax = max(currmax, temp)
        return arr