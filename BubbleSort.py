class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        total_height = 0
        left_height = 0
        right_height = 0
        if root.left != None:
            left_height = 1 + self.getHeight(root.left)
        if root.right != None:
            right_height = 1 + self.getHeight(root.right)
        if left_height > right_height :
            total_height = left_height
        else:
            total_height = right_height
        return total_height

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)