'''
https://leetcode.com/problems/binary-tree-maximum-path-sum/
124. Binary Tree Maximum Path Sum
Hard

===

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000

===

First idea:
    - Map parent child relationships
    - As this is done, recurse at each node in all directions with a guided search style approach
        - guided by non visited nodes, however backtracking to not "block" in other recursive subcalls that can go down the same path.
    - recurse up, left, and right. track the max at every directional turn.`
'''

class Solution:

    def __init__(self):
        self.visited = set();
        self.rel = {  };
        ##self.maxHash = {  };
    
    def rec(self, root):

        ##if root in self.maxHash:
        ##    return self.maxHash[root];

        maxv = root.val;
        self.visited.add(root);

        if root in self.rel and self.rel[root] != None and self.rel[root] not in self.visited:
            maxv = max(maxv, root.val + self.rec(rel[root]));
        if root.left and root.left not in self.visited:
            maxv = max(maxv, root.val + self.rec(root.left));
        if root.right and root.right not in self.visited:
            maxv = max(maxv, root.val + self.rec(root.right));
        
        ##self.maxHash[root] = maxv;
        self.visited.remove(root);
        return maxv;

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0;
        
        stack = [(root, None)];
        res = -(10**7);

        while len(stack):
            child, parent = stack.pop();
            self.rel[child] = parent;

            res = max(res, self.rec(child));

            if child.right:
                stack.append((child.right, child));
            if child.left:
                stack.append((child.left, child));
        
        return res;
