class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = 0 
        curr = head
        while head:
            res = res * 2 + curr.val
            curr = curr.next
        return curr