class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        prevStack = []
        curr = head
        while curr.next is not None:
            prevStack.append(curr)
            curr = curr.next

        result = curr
        while curr is not None:
            if len(prevStack) > 0:
                curr.next = prevStack.pop()
            else:
                curr.next = None
            curr = curr.next
        return result

