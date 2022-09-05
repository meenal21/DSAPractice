import collections
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # using dictionary maintain th level order of any child
        # use dfs to traverse? or bfs? dfs mein traceback stack - bfs mein while loop - but how to maintain the level order of each node?
        # can add a bit to say that the level is over
        # add a string - and then check each time if it is string - 
        
        #code for bfs:
        level = []
        que = collections.deque()
        que.append(root) if root else None
        while que:
            length = len(que)
            ln = []
            for _ in range(length):
                node = que.popleft()
                ln.append(node.val)
                for child in node.children:
                    que.append(child)
            level.append(ln)
        return level
                