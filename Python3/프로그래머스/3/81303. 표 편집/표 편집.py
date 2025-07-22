class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data, prev=self.tail)
            self.tail.next = new_node
            self.tail = new_node

def solution(n, k, cmd):
    dll = DoubleLinkedList()
    nodes = []

    for i in range(n):
        dll.append(i)
        if i == 0:
            nodes.append(dll.head)
        else:
            nodes.append(nodes[-1].next)

    cursor = nodes[k]
    removed = []

    for c in cmd:
        if c[0] == "U":
            x = int(c.split()[1])
            for _ in range(x):
                cursor = cursor.prev

        elif c[0] == "D":
            x = int(c.split()[1])
            for _ in range(x):
                cursor = cursor.next

        elif c[0] == "C":
            removed.append(cursor)
            prev, nxt = cursor.prev, cursor.next

            if prev:
                prev.next = nxt
            else:
                dll.head = nxt

            if nxt:
                nxt.prev = prev
            else:
                dll.tail = prev

            cursor = nxt if nxt else prev

        elif c[0] == "Z":
            node = removed.pop()
            prev, nxt = node.prev, node.next

            if prev:
                prev.next = node
            else:
                dll.head = node

            if nxt:
                nxt.prev = node
            else:
                dll.tail = node

    result = ['O'] * n
    for node in removed:
        result[node.data] = 'X'

    return ''.join(result)
