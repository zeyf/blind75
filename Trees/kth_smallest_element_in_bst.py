'''
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
230. Kth Smallest Element in a BST
Medium

===

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

===

First idea:
    - Iterative Inorder. Return kth node value (1 indexed)

    Time Complexity: O(k)
    Space Complexity: O(k)
'''

# First idea solution
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return False;

        seen = set();
        stack = [root];

        while len(stack):
            c = stack[-1];
            while c and c not in seen:
                seen.add(c);
                c = c.left;
                if c:
                    stack.append(c);
            
            k -= 1;
            node = stack.pop();
            if k == 0:
                return node.val;

            if node.right:
                stack.append(node.right);