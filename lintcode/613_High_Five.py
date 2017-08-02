#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
import heapq


class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        student = dict()
        for std in results:
            if std.id in student:
                heapq.heappush(student[std.id], -std.score)
            else:
                student[std.id] = [-std.score]

        ans = dict()
        for id, hp in student.items():
            sum = 0
            for _ in range(5):
                sum += -heapq.heappop(hp)
            ans[id] = sum / 5.0

        return ans
