# Definition for a binary tree node.
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.dic = defaultdict(list)
        
        
    def dfs(self, node: Optional[TreeNode], level: int):
        if node!= None:
            self.dic[level].append(node.val)
            self.dfs(node.left, level+1)
            self.dfs(node.right,level+1)
    
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.dfs(root,0)
        sol = []
        i = 0
        while i in self.dic:
            leng = len(self.dic[i])
            tot = sum(self.dic[i])
            totfloat = round(tot/leng, 5)
            sol.append(totfloat)
            i += 1
        return sol
                
            