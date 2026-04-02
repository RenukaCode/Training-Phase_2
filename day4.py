def fn(n):
    if n:
        print(n)
    fn(n-1)
fn(5)
# Infinite loop


def fn(n):
    print(n)
    if n:
        print(n)
        return n
        fn(n-1)
fn(5)
# 5
# 5


#recrusive call
def fn(n):
    if n == 0:
        return
    print(n)
    fn(n-1)
    print(n)
fn(3)
# 3
# 2
# 1
# 1
# 2
# 3



# Tree creation, insertion and traversal
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,root,data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left,data)
        else:
            root.right = self.insert(root.right, data)
        return root

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end= " ")
            self.inorder(root.right)

datas = [20,9 ,5 ,15, 17,  32, 25,  23, 29, 30, 35 ,40  ]
sai = BST()
for data in datas:
    sai.root = sai.insert(sai.root , data)
sai.inorder(sai.root)
# 5 9 15 17 20 23 25 29 30 32 35 40 




# Binary Search Tree Insertion, Deletion and Traversal
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,root,data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left,data)
        else:
            root.right = self.insert(root.right, data)
        return root

    def min(self,root):
        while root.left:
            root = root.left
        return root.data
    
    def max(self,root):
        while root.right:
            root = root.right
        return root.data

    def delete(self,root,data):
        if data < root.data:
            root.left = self.delete(root.left , data)
        elif data> root.data:
            root.right = self.delete(root.right , data)
        else:

            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            min_val = self.min(root.right)
            root.data = min_val
            root.right = self.delete(root.right,min_val)
        return root

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end= " ")
            self.inorder(root.right)

datas = [20,9 ,5 ,15, 17,  32, 25,  23, 29, 30, 35 ,40  ]
sai = BST()
for data in datas:
    sai.root = sai.insert(sai.root , data)
sai.inorder(sai.root)   # 5 9 15 17 20 23 25 29 30 32 35 40 
sai.root  = sai.delete(sai.root,20)
print()
sai.inorder(sai.root)   # 5 9 15 17 23 25 29 30 32 35 40 

