# PART_3 List
# 206. Reverse Linked List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        curr = head
        leftList = None
        while curr:
            temp = curr.next
            curr.next = leftList
            leftList = curr
            curr = temp
        return leftList
