class MyHashSet:
    def __init__(self):
        self.my_dict = []

    def add(self, key: int) -> None:
        if key not in self.my_dict:
            self.my_dict.append(key)
    def remove(self, key: int) -> None:
        if key in self.my_dict:
            self.my_dict.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.my_dict:
                return True
        return False