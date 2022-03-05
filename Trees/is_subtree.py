'''
https://leetcode.com/problems/subtree-of-another-tree/
572. Subtree of Another Tree
Easy

===

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104

===

First idea:
    - leverage same tree problem code for comparison when root.val == subRoot.val
    - Recursive

    Time Complexity: O(n)
    Space Complexity: O(n)

'''

class Solution:

    def compare(self, root, subRoot):
        if not root and not subRoot:
            return True;
        elif not root or not subRoot:
            return False;
        elif root.val != subRoot.val:
            return False;
        return self.compare(root.left, subRoot.left) and self.compare(root.right, subRoot.right);

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False;

        left, right = self.isSubtree(root.left, subRoot), self.isSubtree(root.right, subRoot);
        if root.val == subRoot.val:
            if self.compare(root, subRoot):
                return True;

        return left or right;