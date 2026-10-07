# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next or not head.next.next:
            return None
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        #reverse second half

        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        #Change links

        front = head
        back = prev

        while back:
            front_temp = front.next
            back_temp = back.next
            front.next = back
            back.next = front_temp
            front = front_temp
            back = back_temp
        
        


        
        
        