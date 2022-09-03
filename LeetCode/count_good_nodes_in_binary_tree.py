# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def __init__(self):
        self.count = 0
    
    def dfs(self, node: TreeNode, maxval: int):
        if node!= None:
            if maxval <= node.val:
                maxval = node.val
                self.count += 1
                # change the value of maxval and increase the number of good nodes
            # now call both left and right child nodes for dfs
            self.dfs(node.left, maxval)
            self.dfs(node.right,maxval)
        else:
            return
    
    def goodNodes(self, root: TreeNode) -> int:
        maxval = root.val
        self.dfs(root, maxval)
        return  self.count
        
        