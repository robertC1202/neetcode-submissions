# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        #Create dummy node:

        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:

            #get values from lists:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            #compute the sum
            val = val1 + val2 + carry

            #extra carry if any
            carry = val // 10

            #extra second digit if there was a carry
            #If there was not a carry val % 10 would just give that value
            #If there was a carry val % 10 would give the second digit
            val = val % 10

            #Create the new node with the new value
            curr.next = ListNode(val)


            #Update your pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
            


            



        

            
        