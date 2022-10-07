#Merge two sorted linked list
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()  #we need to remember the start that will be next of the dummy
        tail = dummy

        while list1 and list2:#while list1 and list2 different from None
            if list1.val < list2.val:#if val 1 < val 2
                tail.next = list1  # next of the new list will be list 1
                list1 = list1.next  # update pointer of list 1
            else: #same for list 2
                tail.next = list2
                list2 = list2.next
            tail = tail.next  # update pointer of new list

        if list1:  #if list 1 still exist or list 2 still exists add the remaining elements
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next  # the start will be dummy.next