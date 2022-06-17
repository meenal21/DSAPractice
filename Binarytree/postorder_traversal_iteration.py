class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

def postorder_traversal(node):
    stack = []
    current = node 
    while current!=None:
        stack.append(current)
        current = current.left
    
    while stack:
        ele = stack.pop()
        current = ele.right
        while current!=None:
            stack.append(current)
            current = current.left
        
        
    print(stack[::-1])


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

postorder_traversal(root)