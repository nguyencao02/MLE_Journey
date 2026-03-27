from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int)-> int:
        queue = deque()
        for i in range(len(tickets)):
            queue.append([tickets[i],i])
        current_person = queue.popleft()
        current_person[0] = -1
        time += 1
        while queue:
            if current_person[1] == k and current_person[0] == 0:
                return time
            if current_person[0] > 0:
                queue.append(current_person)
        return time