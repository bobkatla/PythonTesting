class DoublyList:
    class __Node:
        def __init__(self, data):
            if type(data) is not int:
                raise Exception("This list only accept integer values")

            self.data = data
            self.next = None
            self.prev = None

    __count = 0
    __head = None
    __tail = None

    def empty(self):
        return True if self.__count == 0 else False

    def start_list(self, data):
        if self.empty():
            new_node = self.__Node(data)
            self.__head = new_node
            self.__tail = new_node
            self.__count += 1
            return True
        else:
            return False

    def add_tail(self, data):
        if not self.start_list(data):
            new_node = self.__Node(data)
            self.__tail.next = new_node
            new_node.prev = self.__tail
            self.__tail = new_node
            self.__count += 1

    def add_head(self, data):
        if not self.start_list(data):
            new_node = self.__Node(data)
            self.__head.prev = new_node
            new_node.next = self.__head
            self.__head = new_node
            self.__count += 1

    def insert(self, data, index):
        if not self.start_list(data):
            if abs(index) > self.__count:
                raise IndexError
            if index < 0:
                index += self.__count
            if index == 0:
                self.add_head(data)
            elif index == self.__count:
                self.add_tail(data)
            else:
                i = 1
                cur = self.__head
                while i < index:
                    cur = cur.next
                    i += 1
                new_node = self.__Node(data)
                cur.next.prev = new_node
                new_node.next = cur.next
                cur.next = new_node
                new_node.prev = cur
                self.__count += 1

    def peek_head(self):
        return self.__head.data

    def peek_tail(self):
        return self.__tail.data

    def get_len(self):
        return self.__count

    def to_list(self) -> list:
        result = []
        cur = self.__head
        while cur is not None:
            result.append(cur.data)
            cur = cur.next
        return result
