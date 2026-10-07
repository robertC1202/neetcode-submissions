# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #Only work with list of 3 nodes
        if not head or not head.next or not head.next:
            return None
        
        #Find middle of the list:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #Reverse second Half of the list
        nextNode = slow.next
        slow.next = None

        prev = None
        curr = nextNode

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        #Create the new list by using four pointers

        front = head
        back = prev

        while back:
            nextFront = front.next
            nextBack = back.next
            front.next = back
            back.next = nextFront
            front = nextFront
            back = nextBack
        
        


        
        
        