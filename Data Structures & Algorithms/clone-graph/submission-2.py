"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        oldToCopy={}
        oldToCopy[node]=Node(node.val)
        q=deque([node])

        while q:
            curr=q.popleft()
            for n in curr.neighbors:
                if n not in oldToCopy:
                    oldToCopy[n]=Node(n.val)
                    q.append(n)
                oldToCopy[curr].neighbors.append(oldToCopy[n])
        return oldToCopy[node]

        #Time: O(V+E)
        #Space: O(V)
        