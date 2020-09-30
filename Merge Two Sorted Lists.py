# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l1None = l1 is None
        l2None = l2 is None

        if l1None and l2None:
            return None
        if l1None and not l2None:
            return l2
        if not l1None and l2None:
            return l1

        if l1.val < l2.val:
            head = l1
            curr1 = l1.next
            curr2 = l2
        else:
            head = l2
            curr1 = l1
            curr2 = l2.next

        curr = head
        while curr1 is not None and curr2 is not None:
            if curr1.val < curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next

        curr.next = curr1 or curr2
        return head
