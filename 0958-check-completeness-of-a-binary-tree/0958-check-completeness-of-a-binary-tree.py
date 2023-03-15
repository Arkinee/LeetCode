# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        hasToNone = False
        queue.append(root)
        
        while(queue):
            temp = queue.popleft()
            print(temp.val)

            if(temp.left == None and temp.right != None):
                return False
            elif(temp.left != None and temp.right != None):
                if(hasToNone): return False
                queue.append(temp.left)
                queue.append(temp.right)
            elif(temp.left == None and temp.right == None):
                hasToNone = True
            elif(temp.left != None and temp.right == None):
                if(hasToNone): return False
                hasToNone = True
                if(temp.left != None): queue.append(temp.left)
                if(temp.right != None): queue.append(temp.right)
            

        return True

        
        