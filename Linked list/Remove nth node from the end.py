# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #SOLUTION WITH TWO POINTER LEFT AND RIGHT
        #left start from start -1 so we found the previous node from the one we need to remove
        #right start from n node so when we reach the end we know that L next is the node we want to remove
        dummy = ListNode()
        dummy.next = head
        count = 0
        right = head
        while right and count < n:
            right = right.next
            count += 1

        left = dummy
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
        #or recursive we reach the end and count
        count = 0
        temp = None

        def ric(node):
            nonlocal count
            nonlocal temp
            if node:
                ric(node.next)
                count += 1
                if count == n:
                    temp = node
                if count == n + 1:
                    node.next = node.next.next

        if head.next is None and n > 0:
            return None
        else:
            count = 0
            ric(head)
            if temp == head and count == n:
                head = head.next

            return head