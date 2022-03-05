'''
https://leetcode.com/problems/invert-binary-tree/
226. Invert Binary Tree
Easy

===

Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

===

First Idea:
    - Iterative preorder left right swap.

    Time Complexity: O(n)
    Space Complexity: O(n)
'''

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None;
        
        stack = [root];
        while len(stack):
            node = stack.pop();

            t = node.left;
            node.left = node.right;
            node.right = t;

            if node.right:
                stack.append(node.right);
            if node.left:
                stack.append(node.left);
        return root;