# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        count = 0
        if root == None:
            return count

        data = [root]
        while len(data) != 0:
            curr = data.pop()
            if L <= curr.val <= R:
                count += curr.val
            if L < curr.val and curr.left is not None:
                data.append(curr.left)
            if R > curr.val and curr.right is not None:
                data.append(curr.right)
        return count