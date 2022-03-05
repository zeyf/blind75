'''
https://leetcode.com/problems/binary-tree-level-order-traversal/
102. Binary Tree Level Order Traversal
Medium

===

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

===

First idea:
    - Full Levelwise order BFS.

    Time Complexity: O(n)
    Space Complexity: O(n)
'''

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return [];
        
        q = [root];
        levels = [];
        
        while len(q):
            size = len(q);
            levels.append([]);
            while size:
                node = q.pop(0);
                levels[-1].append(node.val);
                if node.left:
                    q.append(node.left);
                if node.right:
                    q.append(node.right);
                size -= 1;
        return levels;