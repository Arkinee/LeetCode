# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum = 0
    temp = ""
    arr = []
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.arr = []
        self.recursive(root)
        for i in self.arr:
            self.sum += int(i)
            print(int(i))
        return self.sum
    

    def recursive(self, root: Optional[TreeNode]):
        self.temp += str(root.val)
        #print(self.temp)
        isLeft = False
        isRight = False

        if(root.left != None):
            self.recursive(root.left)
            isLeft = True
        
        if(root.right != None):
            self.recursive(root.right)
            isRight = True
        
        #if(root.left == None and root.right == None):
        if(not isLeft and not isRight):
            self.arr.append(self.temp)
            self.temp = self.temp[0:len(self.temp)-1]

        if(isLeft or isRight):
            self.temp = self.temp[0:len(self.temp)-1]