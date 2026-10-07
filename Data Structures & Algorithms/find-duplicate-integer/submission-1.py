class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        

        #To find a cycle in an array we have to replicate using slow and fast pointer
        #Slow pointer in an array moves once by doing slow = nums[slow]
        #Fast pointer in an array moves twice by doing fast = nums[nums[fast]] 
        #this works if both fast and slow are first initialized to 0
        slow = fast = 0


        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            #if they slow ever equals fast, we found that there is a cycle
            #slow and fast are also at the point of intersection at this point
            #Just break whenever they are equal to each other
            if slow == fast:
                break
        
        #To find the number that is a duplicate you need to find the start of the cycle
        #The start of the cycle is the duplicate number
        #Create another slow pointer that starts at 0
        #move both slow2 and slow by 1 each and they eventually will equal to each other.
        #At that point, return either slow or slow2

        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                return slow2




        
        