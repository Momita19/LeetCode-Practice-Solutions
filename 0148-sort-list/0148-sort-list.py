# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        mid = self.findMiddle(head)
        left = head
        right = mid.next
        mid.next = None

        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)

        return self.mergeSort(left_sorted, right_sorted)

    def findMiddle(self, head):
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def mergeSort(self, left, right):
        dummy = ListNode(0)
        curr = dummy

        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next

            curr = curr.next

        if left:
            curr.next = left
        if right:
            curr.next = right

        return dummy.next

        