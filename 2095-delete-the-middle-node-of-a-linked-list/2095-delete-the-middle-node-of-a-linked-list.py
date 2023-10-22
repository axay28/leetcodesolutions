# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head.next
        fast, slow = head.next.next, head # FAST =4, SLOW =1
        while fast and fast.next: 
            slow = slow.next #3 4
            fast = fast.next.next#1 6
        slow.next = slow.next.next #1 
        return head
        