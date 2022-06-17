class Node:

    def __init__(self,value,parent=None,left=None,right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

def find_level_order(rootN):
    queue = []
    queue.append(rootN)

    while queue:
        ele = queue.pop()
        if ele!=None:
            print(ele.value)
            queue.append(ele.right)
            queue.append(ele.left)


root = Node(1)
root.right = Node(3)
root.left = Node(2)
find_level_order(root)

