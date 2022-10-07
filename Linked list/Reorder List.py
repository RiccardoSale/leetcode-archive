"""""
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow, fast = head, head
        while fast and fast.next:#slow pointer and fast pointer method
            slow = slow.next
            fast = fast.next.next
        # reverse second half

        second = slow.next
        prev = slow.next = None
        #slow next at None because it become the last element in the list it nedd to point to None
        #reverse second half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev #head and head of the reverse list
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2