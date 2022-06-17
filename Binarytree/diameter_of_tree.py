class Node:

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        

def get_height_dfs(node,height):
    if node!=None:
        height += 1
        height1 = get_height_dfs(node.left,height)
        height2 = get_height_dfs(node.right,height)
        return max(height1,height2)
    else:
        return height

def get_diameter(rootNode):
    h1 = get_height_dfs(rootNode.left,0)
    h2 = get_height_dfs(rootNode.right,0)
    diameter = h1 + h2 + 1
    print(diameter)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.left = Node(5)
get_diameter(root)
