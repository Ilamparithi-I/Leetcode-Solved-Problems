class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        count = 1
        middle = head
        curr = head
        while(curr.next != None):
            curr = curr.next
            count += 1
            if count%2 == 0 and count > 2:
                middle = middle.next
        middle.next = middle.next.next
        return head