class Node:

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(node):
    stack = []
    #stack.append(node)
    current = node
    while current!=None:
        stack.append(current)
        current = current.left

    while stack:
        ele = stack.pop()
        print(ele.value)
        current = ele.right
        while current!=None:
            stack.append(current)
            current = current.left

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

inorder_traversal(root)