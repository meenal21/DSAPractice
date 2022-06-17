class Node:
    
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

def reverse_level_order(rootN):
    queue = []
    stack = []

    queue.append(rootN)

    while queue:
        ele = queue.pop()
        if ele!=None:
            stack.append(ele.value)
            queue.append(ele.left)
            queue.append(ele.right)

    print(stack[::-1])

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(60)

reverse_level_order(root)

