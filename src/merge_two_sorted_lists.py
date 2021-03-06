# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def append(self, li):
        curr = self
        for i in li:
            curr.next = ListNode(i)
            curr = curr.next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        res = ListNode(None)
        curr = res

        # while 1:
        #     if not l1:
        #         curr.next = l2
        #         break
        #
        #     if not l2:
        #         curr.next = l1
        #         break
        #
        #     curr.next = ListNode(None)
        #     curr = curr.next
        #     if l1.val <= l2.val:
        #         curr.val = l1.val
        #         l1 = l1.next
        #     else:
        #         curr.val = l2.val
        #         l2 = l2.next

        while l1 and l2:
            curr.next = ListNode(None)
            curr = curr.next
            if l1.val <= l2.val:
                curr.val = l1.val
                l1 = l1.next
            else:
                curr.val = l2.val
                l2 = l2.next
        if not l1:
            curr.next = l2

        if not l2:
            curr.next = l1

        return res.next

if __name__ == '__main__':
    solution = Solution()

    l1 = ListNode(1)
    l1.append([2,3,4])

    l2 = ListNode(1)
    l2.append([2, 3, 4, 5, 6])

    a = solution.mergeTwoLists(l1, l2)
    while a:
        print(a.val)
        a = a.next
