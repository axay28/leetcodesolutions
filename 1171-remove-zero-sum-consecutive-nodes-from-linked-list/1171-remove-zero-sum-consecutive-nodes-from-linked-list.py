# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initialize dummy
        # make sure current sum is tracked
        # when it reaches zero 
        # next pointer manipulation
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head:
            current = head
            total = 0
            while current:
                total += current.val
                if total == 0:
                    prev.next = current.next
                current = current.next
            prev = head
            head = head.next

        return dummy.next

                