class Solution:
    def countSeniors(self, details: list[str]) -> int:
        count_senior = 0
        for p in details:
            age = int(p[11:13])
            if age > 60:
                count_senior += 1
        return count_senior