# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None or head.next.next == None:
            return head
        currE = head.next
        currO = head
        headE = head.next
        while (True):
            if currE.next == None:
                currO.next = headE
                break
            if currE.next.next == None:
                currO.next = currE.next
                currE.next.next = headE
                currE.next = None
                break
            currO.next = currE.next
            currE.next = currE.next.next
            currO = currO.next
            currE = currE.next
        return head

        