# Valid Paranthesis
def isValid(s):
    stack = []
    for val in s:
        if val == '(': stack.append(')')
        elif val == '[': stack.append(']')
        elif val == '{': stack.append('}')
        elif len(stack) == 0 or stack.pop() != val:
            return False
    return len(stack) == 0
print(isValid("{[]()}")) # True
print(isValid("[}]()"))  # False



# https://leetcode.com/problems/decode-string/
def decodeString(s):
    stack = []
    for val in s:
        if val != "]":
            stack.append(val)
        else:
            ch = ""
            if stack[-1] != "[":
                ch = stack.pop() + ch
            stack.pop()
            nums = ""
            while len(stack) and stack[-1].isdigit():
                nums = stack.pop() + nums
            stack.append(ch * int(nums))
    return "".join(stack)
print(decodeString("3[a]2[bc]")) # "aaabcbc"
print(decodeString("3[a2[c]]"))  # "accaccacc"




#  Creation, insertion and deletion of nodes in Linkedlist
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_b(self,data):
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def insert_e(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = newnode



    def insert_by_position(self,pos,data):
        if pos == 0:
            self.insert_b(data)
            return
        newnode = Node(data)
        cur = self.head
        for i in range(pos-1):
            if cur.next is None:
                break
            cur = cur.next

        newnode.next = cur.next
        cur.next = newnode


    def delete_b(self):
        if self.head:
            self.head = self.head.next


    def delete_e(self):
        if self.head:
            if self.head.next is None:
                self.head = None
                return
            cur = self.head
            while cur.next.next:
                cur = cur.next
            cur.next = None


    def delete_by_position(self,pos):
        pass

    def display(self):
        cur = self.head
        while cur:
            print(cur.data,end="->")
            cur = cur.next


anji = Linkedlist()
sadiq = Linkedlist()
anji.insert_b(7)
anji.insert_b(23)
anji.insert_e(5)
anji.display()
anji.insert_by_position(100,67)
print()
anji.display()

