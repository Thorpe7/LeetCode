""" Script for merging two sorted linked lists. """

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, listNode_l1: Optional[ListNode], listNode_l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # Need to wrap brain around idea that we are pointing and arranging nodes
        # Don't need to handle the values in the nodes, just arranged the nodes themselves

        # Should rename variables from `list1` and `list2` --> listNode_l1 & listNode_l2
        # Framing them as lists is unclear

        head_node = ListNode()
        tail = head_node

        while (listNode_l1) and (listNode_l2):  # why entire listNode not being None?

            if listNode_l1.val < listNode_l2.val:
                tail.next = listNode_l1  # Points to this node now
                listNode_l1 = (
                    listNode_l1.next
                )  # Now focused on the next node from list1
            else:
                tail.next = listNode_l2
                listNode_l2 = listNode_l2.next

            tail = tail.next  # Still shaky on why pointing to next

        if not listNode_l1:
            tail.next = listNode_l2
        if not listNode_l2:
            tail.next = listNode_l1

        return head_node.next
