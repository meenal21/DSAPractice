# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ### dfs and then if child not 0 then stay else remove
        # how to remove - send a flag - true or false
        # true to remove else false
        
        def dfs(node: Optional[TreeNode]) -> bool:
            if node!=None:
                ans = dfs(node.right)
                if ans == True:
                    node.right = None
                
                ans = dfs(node.left)
                if ans == True:
                    node.left = None
                    
                if node.right== None and node.left == None and node.val == 0:
                    return True
                return False
    
        dfs(root)
        if root.val == 0 and root.right == None and root.left == None:
            return None
        
        return root
    
# time complexity = O(n) - traversing every node once
# space complexity = O(H) - height of the tree - worst case - when left skewed or right skewed
