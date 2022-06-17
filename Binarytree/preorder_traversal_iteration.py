from turtle import left


class Node:

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal(node):
    stack = []
    current = node
    while current!=None:
        print(current.value)
        stack.append(current)
        current = current.left
    
    while stack:
        ele = stack.pop()
        current = ele.right
        while current!=None:
            print(current.value)
            stack.append(current)
            current = current.left

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

preorder_traversal(root)