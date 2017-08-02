#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """

    def rehashing(self, hashTable):
        # write your code here
        if not hashTable:
            return []

        capacity = len(hashTable) * 2
        new_ht = [None for _ in range(capacity)]

        for head in hashTable:
            while head:
                tmp = head.next
                slot = head.val % capacity
                if new_ht[slot]:
                    end = new_ht[slot]
                    while end.next:
                        end = end.next
                    head.next = end.next
                    end.next = head
                else:
                    new_ht[slot] = head
                    head.next = None

                head = tmp

        return new_ht
