# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        new=[]
        curr=head
        while curr:
            new.append(curr.val)
            curr=curr.next
            
        new.sort()
        curr=head
        index=0
        while curr:
            curr.val=new[index]
            curr=curr.next
            index+=1
        return head