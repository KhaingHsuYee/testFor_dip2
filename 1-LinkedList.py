
class Node:

    def __init__(self, data, info: str):
        self.data = data
        self.ncc = info
        self.next = None


class Linked:

    def __init__(self):
        self.head = None


if __name__ == "__main__":
    linkedList = Linked()
    linkedList.head = Node(10, "first")

    second = Node(20, "Second")
    third = Node(30, "Third")

    linkedList.head.next = second
    second.next = third
    while linkedList.head is not None:
        print(linkedList.head.data)
        print(linkedList.head.ncc)
        linkedList.head = linkedList.head.next
