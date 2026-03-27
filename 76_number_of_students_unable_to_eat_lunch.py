from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int])-> int:
        student_queue = deque(students)
        sandwiches_stack = deque(sandwiches)
        count = 0
        while student_queue:
            if student_queue[0] == sandwiches_stack[0]:
                student_queue.popleft()
                sandwiches_stack.popleft()
                count = 0
            else:
                student_queue.append(student_queue.popleft())
                count += 1
            if count == len(student_queue):
                break
        return len(student_queue)
            
        
        