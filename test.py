from DoublyList import DoublyList

if __name__ == "__main__":
    l = DoublyList()
    l.add_head(2)
    l.add_head(6)
    l.add_tail(5)
    print(l.to_list())