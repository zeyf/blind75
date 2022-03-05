'''
https://leetcode.com/problems/validate-binary-search-tree/
98. Validate Binary Search Tree
Medium

===

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1

===

First idea:
    - Inorder (either recursive or iterative. will do iterative)
        - store the inorder sequence of tree values
        - no need to sort for a nlogn time complexity.
            - compare two at a time, trailing element is >= than the leading, return False. else True

    Time Complexity: O(n)
    Space Complexity: O(n)
'''

# First idea solution
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False;

        seen = set();
        stack = [root];
        inordersequence = [];
        while len(stack):
            c = stack[-1];
            while c and c not in seen:
                seen.add(c);
                c = c.left;
                if c:
                    stack.append(c);
            
            node = stack.pop();
            inordersequence.append(node.val);
            if node.right:
                stack.append(node.right);
        
        for i in range(len(inordersequence)-1):
            if inordersequence[i] >= inordersequence[i+1]:
                return False;
        return True;


# Slightly more optimized. Does not go through full tree if found to be invalid BST as you traverse the tree.
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False;

        seen = set();
        stack = [root];
        inordersequence = [];
        while len(stack):
            c = stack[-1];
            while c and c not in seen:
                seen.add(c);
                c = c.left;
                if c:
                    stack.append(c);
            
            node = stack.pop();
            if len(inordersequence) == 0:
                inordersequence.append(node.val);
            else:
                if inordersequence[-1] >= node.val:
                    return False;
                inordersequence.append(node.val);
            if node.right:
                stack.append(node.right);
        
        return True;