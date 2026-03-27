from collections import deque
class MyStack:
    def __init__(self):
        self.__items = deque()
    def push(self, x: int)-> None:
        self.__items.append(x)
        for _ in range(len(self.__items)-1):
            self.__items.append(self.__items.popleft())
    def pop(self) -> int:
        if not self.empty:
            return self.__items.popleft()
        return None
    
    def top(self) -> int:
        return self.__item[0] if not self.empty() else None
    
    def empty(self) -> bool:
        return len(self.__items) == 0