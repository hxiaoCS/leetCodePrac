# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        nodes = []

        while curr:
            nodes.append(curr)
            curr = curr.next

        if n == len(nodes):
            tmp = head.next
            head.next = None
            head = tmp
        else:
            tmp = nodes[-n].next
            nodes[-n].next = None
            nodes[-n-1].next = tmp

        return head
