class Solution:
    def addStrings(self, num1:str,num2:str)->str:
        res = []
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        while i >= 0 or j >=0 or carry > 0:
            if i >=0:
                n1 = ord(num1[i]) - ord('0')
            else:
                n1 = 0
            if j >= 0:
                n2 = ord(num2[j]) - ord('0')
            else:
                n2 = 0
                n2 = 0
            total = n1 + n2 + carry
            res.append(str(total%10))
            carry = total // 10
            i -= 1
            j -= 1
        return "".join(res[::-1])     
            
            