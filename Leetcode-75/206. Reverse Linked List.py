# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        prev = None
        curr = head
        while(True):
            temp = curr.next
            curr.next = prev
            if temp == None:
                break
            prev = curr
            curr = temp
        return curr
        