# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return None

        #Find the middle of the list
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #Reverse second half of the list
        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        front = head
        back = prev
        
        #Change links
        while prev:
            nxtFrontVal = front.next
            nxtBackVal = prev.next
            front.next = prev
            prev.next = nxtFrontVal
            front = nxtFrontVal
            prev = nxtBackVal 

        
            

        

        