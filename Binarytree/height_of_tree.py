class Node:
    
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def dfs(node,height):
    
    if node!=None:
        #print(node.value)
        height += 1
        height1 = dfs(node.left,height)
        height2 = dfs(node.right,height)
        #print(height1,height2)
        return max(height1,height2)
    else:
        return height

def height_of_tree(rootN):
    #print(rootN.value)
    height = dfs(rootN,0)
    print(height)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
#root.right.left = Node(4)

height_of_tree(root)
