# 2. Add Two Numbers.py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next: ListNode | None = next

class ListIter:
    def __init__(self, listNode):
        self.listNode = listNode

    def __iter__(self):
        return self

    def __next__(self):
        if self.listNode is None:
            raise StopIteration
        current = self.listNode.val
        self.listNode = self.listNode.next
        return current


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_list = list(ListIter(l1))
        num_list_len = len(num_list)
        for idx, num in enumerate(ListIter(l2)):
            if idx >= num_list_len:
                num_list.append(num)
                continue
            num_list[idx] += num
        result = sum((10 ** i) * num for i, num in enumerate(num_list))

        total, digit = divmod(result, 10)
        original = ListNode(digit)
        node = original
        while total:
            total, digit = divmod(total, 10)
            node.next = ListNode(digit)
            node = node.next
        return original
