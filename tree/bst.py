__author__ = 'ashwin'

# binary search tree in python
"""
user:
bst = Tree()
bst.insert(14)
bst.preorder()
bst.inorder()
bst.postorder()

class
insert (self, data)
find (self, data)
preorder()
postorder()
inorder()

Node :
insert(self, data)
find(self, data)
preorder()
postorder()
inorder()

"""
class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self,data):
        if self.value == data: #this is to check whether there is no duplicate datas in our tree
            return False
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def find(self, data):
        if(self.value == data):
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print (str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print (str(self.value))

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print (str(self.value))
            if self.rightChild:
                self.rightChild.inorder()




class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print("Preorder:")
        self.root.preorder()

    def postorder(self):
        print("postorder:")
        self.root.postorder()

    def inorder(self):
        print("inorder:")
        self.root.inorder()


bst = Tree()
number = raw_input().split(" ")
print(bst.insert(10))
print(bst.insert(15))
print(bst.insert(20))
bst.preorder()