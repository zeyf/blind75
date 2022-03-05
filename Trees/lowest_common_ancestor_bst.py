'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
235. Lowest Common Ancestor of a Binary Search Tree
Easy

===

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.

===

First idea:
    - Hashmap child parent parallel directed edges to traverse back up the tree.
    - Set hash one node's path up to root, first intersection is the LCA.

    Time Complexity: O(n)
    Space Complexity: O(n)

Second idea:
    - No hashmap.
    - Iterates down to p, adding all nodes on path from root to p to a set.
    - Using prev, current two pointer strategy, once current falls upon a node that is not on
        on the path from the root to p, that means that our prev is the LCA since that would be the first divergence,
        and the connecting ancestor is prev, the parent to the current "current" node.

    Time Complexity: O(log(p))
    Space Complexity: O(log(p))
'''



# Second idea solution
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None;
        
        pRootPathSet = set();
        pc = root;
        
        while True:
            pRootPathSet.add(pc);

            if p.val > pc.val:
                pc = pc.right;
            elif p.val < pc.val:
                pc = pc.left;
            else:
                break;

        c, prev = root, None;
        while True:
            prev = c;
            if q.val > c.val:
                c = c.right;
            elif q.val < c.val:
                c = c.left;
            else:
                break;
        
            if c not in pRootPathSet:
                return prev;
        return prev;
        