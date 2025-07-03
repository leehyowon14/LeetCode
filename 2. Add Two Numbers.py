# 2. Add Two Numbers.py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next: ListNode | None = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_num = [l1.val]
        while l1.next is not None:
            l1 = l1.next
            first_num.append(l1.val)

        second_num = [l2.val]
        while l2.next is not None:
            l2 = l2.next
            second_num.append(l2.val)

        result = sum((10 ** i) * num for i, num in enumerate(first_num)) + \
            sum((10 ** i) * num for i, num in enumerate(second_num))

        total, digit = divmod(result, 10)
        original = ListNode(digit)
        node = original
        while total:
            total, digit = divmod(total, 10)
            node.next = ListNode(digit)
            node = node.next
        return original
