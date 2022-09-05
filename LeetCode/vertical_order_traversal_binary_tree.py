from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    
    def dfs(self, node: Optional[TreeNode],col: int, row: int):
        if node!= None:
            if col in self.dic:
                (self.dic[col])[row].append(node.val)
            else:
                dcnew = defaultdict(list)
                self.dic[col] = dcnew
                (self.dic[col])[row].append(node.val)
            self.dfs(node.left, col-1, row+1)
            self.dfs(node.right,col+1,row+1)
        
        
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dic = defaultdict()
        self.dfs(root,0,0)
        vot = []
        for i in sorted(self.dic.keys()):
            num = []
            for j in sorted(self.dic[i].keys()):
                (self.dic[i])[j].sort()
                for k in (self.dic[i])[j]:
                    num.append(k)
            vot.append(num)
        return vot