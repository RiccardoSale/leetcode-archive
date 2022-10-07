# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None

        while curr:
            temp = curr.next  #save the next element
            curr.next = prev # curr.next will be equal to prev ( first time None )
            prev = curr  # prev will be equal to curr think about the draw and the arrow
            curr = temp  # curr will be equal to temp that we saved before , we need to save it because we dont have the link anymore
        return prev
