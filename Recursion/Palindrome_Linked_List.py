# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    valueStore = []
    def isPalindrome(self, head, count = 0):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if count == 0 and head.next is None:
            return True
        valueStore.append(head.val)
        self.isPalindrome(head= head.next, count= count + 1)