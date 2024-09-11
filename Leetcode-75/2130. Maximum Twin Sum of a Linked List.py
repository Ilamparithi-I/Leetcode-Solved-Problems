# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        val = []
        while(fast != None):
            val.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        maxval = 0
        for i in range(len(val)-1, -1, -1):
            cur = val[i]+slow.val
            if cur > maxval:
                maxval = cur
            slow = slow.next
        return maxval