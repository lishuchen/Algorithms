#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2
    def addLists2(self, l1, l2):
        # Write your code here
        len_one = 0
        n_l1 = l1
        while n_l1:
            n_l1 = n_l1.next
            len_one += 1

        len_two = 0
        n_l2 = l2
        while n_l2:
            n_l2 = n_l2.next
            len_two += 1

        dummy = ListNode(0)
        start = l = dummy
        for _ in range(abs(len_one - len_two)):
            if l1 or l2:
                if len_one > len_two:
                    if l1:
                        val = l1.val
                        l1 = l1.next
                else:
                    if l2:
                        val = l2.val
                        l2 = l2.next
                l.next = ListNode(val)
                l = l.next

        flag, node = self.add(l1, l2)
        if l == dummy:
            if flag == 1:
                new_node = ListNode(1)
                new_node.next = node
                node = new_node
        else:
            l.val += flag

        l.next = node

        return dummy.next

    def add(self, l1, l2):
        if l1 is None or l2 is None:
            return (0, None)

        flag, next_node = self.add(l1.next, l2.next)
        val = flag + l1.val + l2.val
        flag, v = divmod(val, 10)
        node = ListNode(v)
        node.next = next_node

        return (flag, node)
