# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Given a binary tree, return all root-to-leaf paths.

# For example, given the following binary tree:

#   1
# /   \
# 2     3
# \
#   5
# All root-to-leaf paths are:

# ["1->2->5", "1->3"]


class Solution(object):
    def binaryTreePaths(self, root):
        if root == None:
            return []
        elif root.left == None and root.right == None:
            return [str(root.val)]
        else:
            leftPaths = self.binaryTreePaths(root.left)
            rightPaths = self.binaryTreePaths(root.right)
            fullPath = leftPaths + rightPaths
            
            finalList = []
            for leaf in fullPath: 
                finalList.append(str(root.val) + "->" + str(leaf))
            
        return finalList
            
        
