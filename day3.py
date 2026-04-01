# Double LinkedList
# Creation, Insertion, Deletion of Nodes
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_b(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
            return
        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode

    def insert_e(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
            return
        self.tail.next = newnode
        newnode.prev = self.tail
        self.tail = newnode

    def delete_b(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_e(self, data):
        newnode = Node(data)
        if self.tail is None:
            self.tail = newnode
            return
        self.tail = self.tail.prev
        self.tail.next = None

    def delete_pos(self,pos):
        if pos == 0:
            self.delete_b()
            return
        if self.head:
            cur = self.head
            for i in range(pos):
                cur = cur.next
            if cur is self.tail:
                self.delete_e()
                return
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

    def display_forward(self):
        cur = self.head
        while cur:
            print(cur.data,end="->")
            cur = cur.next

    def display_backward(self):
        cur = self.tail
        while cur:
            print(cur.data,end="->")
            cur = cur.prev
anji = LinkedList()
anji.insert_b(7)
anji.insert_b(23)
anji.insert_b(5)
anji.insert_e(8)
anji.display_forward()
print()
anji.display_backward()
anji.delete_pos(2)
print()
anji.display_forward()
print()
anji.display_backward()




# https://leetcode.com/problems/middle-of-the-linked-list/
def middleNode(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow



# https://leetcode.com/problems/reverse-linked-list/
def reverse(head):
    node = None
    while head:
        temp = head.next
        head.next = node
        node = head
        head = temp
    return node


# https://leetcode.com/problems/merge-two-sorted-lists/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Sol:
    def mergeLists(l1,l2):
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
        cur.next = l1 or l2
        return dummy.next
