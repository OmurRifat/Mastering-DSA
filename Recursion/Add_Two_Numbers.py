# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution with recursion
class Solution(object):
    def addTwoNumbers(self, l1, l2, carry=0):
        # base case: if no more nodes and no carry, stop recursion
        if not l1 and not l2 and not carry:
            return None
        
        # assigning the node value; assigned 0 if node is none
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # calculating sum and carry
        sum = val1 + val2 + carry
        carry = sum // 10
        digit = sum % 10

        # creating new node by the extracted digit
        newNode = ListNode(digit)

        # recursive case: recursively calling the next node along with the carry
        newNode.next = self.addTwoNumbers(l1.next if l1 else None, l2.next if l2 else None, carry)

        return newNode
    



# Solution without recursion
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummyNode = ListNode(0)
        current = dummyNode
        carry = 0

        while l1 or l2 or carry != 0:

            # assigning the node value; assigned 0 if node is none
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # calculating sum and carry
            sum = val1 + val2 + carry
            carry = sum // 10
            digit = sum % 10

            current.next = ListNode(digit)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummyNode.next