'''
https://leetcode.com/problems/merge-k-sorted-lists/
23. Merge k Sorted Lists
Hard

===

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.

===

First Idea:
    - use a min heap to take in all the values and pop them to build out a new sorted list.

'''

import heapq as heaper;

# First idea solution
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [];
        for linkedlist in lists:
            c = linkedlist;
            while c:
                heaper.heappush(heap, c.val);
                c = c.next;
        dummy = ListNode(-1);
        temp = dummy;
        while len(heap):
            temp.next = ListNode(heaper.heappop(heap));
            temp = temp.next;
        return dummy.next;