class Node:
    """结点"""

    def __init__(self, val):
        self.elem = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.__head = None  # 头节点

    def length(self):
        """返回链表长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1
        return count

    def traval(self):
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def get(self, index: int) -> int:
        """
        获取链表中第 index 个节点的值。如果索引无效，则返回-1。
        """
        if 0 <= index < self.length():
            cur = self.__head
            for i in range(index):
                cur = cur.next
            return cur.elem
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
        """
        node = Node(val)
        if self.__head is None:
            self.__head = node
        else:
            node.next = self.__head
            self.__head = node
            node.next.prev = node

    def addAtTail(self, val: int) -> None:
        """
        将值为 val 的节点追加到链表的最后一个元素。
        """
        node = Node(val)
        if self.__head is None:
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def addAtIndex(self, index: int, val: int) -> None:
        """
        在链表中的第 index 个节点之前添加值为val的节点。如果index等于链表的长度，则该节点将附加到链表的末尾。如果index大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
        """
        node = Node(val)
        if index <= 0:
            self.addAtHead(val)
        elif index == self.length():
            self.addAtTail(val)
        elif index > self.length():
            pass
        else:
            cur = self.__head
            for i in range(index):
                cur = cur.next
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def deleteAtIndex(self, index: int) -> None:
        """
        如果索引 index 有效，则删除链表中的第 index 个节点。
        """
        cur = self.__head
        if index == 0:
            self.__head = cur.next
        elif 0 < index < self.length() - 1:
            for i in range(index):
                cur = cur.next
            cur.next.prev = cur.prev
            cur.prev.next = cur.next
        elif index == self.length() - 1:
            for i in range(index):
                cur = cur.next
            cur.prev.next = cur.next


# ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex",
# "addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
# [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]

obj = MyLinkedList()
obj.traval()
obj.addAtHead(7)
obj.traval()
obj.addAtHead(2)
obj.traval()
obj.addAtHead(1)
obj.traval()
obj.addAtIndex(3, 0)
obj.traval()
obj.deleteAtIndex(2)
obj.traval()
obj.addAtHead(6)
obj.traval()
obj.addAtTail(4)
obj.traval()
print(obj.get(4))
obj.traval()
obj.addAtHead(4)
obj.traval()
obj.addAtIndex(5, 0)
obj.traval()
obj.addAtHead(6)
obj.traval()