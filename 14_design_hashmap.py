class MyHashMap:
    def __init__(self):
        self.my_dict = []

    def put(self, key: int, value: int) -> None:
        for pair in self.my_dict:
            if pair[0] == key:
                pair[1] = value
                return
        self.my_dict.append([key,value])

    def get(self, key: int) -> int:
        for pair in self.my_dict:
            if pair[0] == key:
                return pair[1]
        return -1
    def remove(self, key: int) -> None:
        for pair in self.my_dict:
            if pair[0] == key:
                self.my_dict.remove(pair)
                return