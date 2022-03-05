
'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/

===

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

===

First idea:
    - Recursive DFS approach, take max of left and right, add 1 at each node for level incrementation.

    Time Complexity: O(n)
    Space Complexity: O(n)

Second idea:
    - Iterative DFS/BFS approach. Use tuples in the stack, with depth starting at 1 at the root.
    Time Complexity: O(n)
    Space Complexity: O(n)

Third idea:
    - Levelwise BFS approach. tuples not needed with level counter.
    Time Complexity: O(n)
    Space Complexity: O(n)
'''

# First idea solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0;

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right));

# Second idea solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0;
        
        stack, res = [(root, 1)], 1;
        while len(stack):
            node, depth = stack.pop();
            res = max(res, depth);

            if node.right:
                stack.append((node.right, depth + 1));
            if node.left:
                stack.append((node.left, depth + 1));
        
        return res;


# Third idea solution

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0;
        
        q = [root];
        res = 1;

        while len(q):
            size = len(q);
            while size:
                node = q.pop(0);
                if node.right:
                    q.append(node.right);
                if node.left:
                    q.append(node.left);
                size -= 1;
            
            if len(q) > 0:
                res += 1;

        return res;