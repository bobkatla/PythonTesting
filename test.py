from DoublyList import DoublyList

if __name__ == "__main__":
    l = DoublyList()
    l.add_head(2)
    l.add_head(6)
    l.add_tail(5)
    l.insert(10, 0)
    l.insert(34, 1)
    l.insert(23, 1)
    l.insert(333, -6)
    print(l.to_list())
    # print(l.peek(-6))
