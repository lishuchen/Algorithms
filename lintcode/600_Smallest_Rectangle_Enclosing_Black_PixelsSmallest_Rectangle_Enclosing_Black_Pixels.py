#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    # @param image {List[List[str]]}  a binary matrix with '0' and '1'
    # @param x, y {int} the location of one of the black pixels
    # @return an integer
    def minArea(self, image, x, y):
        # Write your code here
        if not image:
            return 0

        start, end, mid = 0, x, 0

        while start < end:
            mid = (start + end) >> 1
            if "1" in image[mid]:
                end = mid
            else:
                start = mid + 1
        up = start

        start, end, mid = x, len(image) - 1, 0
        while start < end:
            mid = ((start + end) >> 1) + 1
            if "1" in image[mid]:
                start = mid
            else:
                end = mid - 1
        down = start

        start, end, mid = 0, y, 0
        while start < end:
            mid = (start + end) >> 1
            if "1" in [row[mid] for row in image]:
                end = mid
            else:
                start = mid + 1
        left = start

        start, end, mid = y, len(image[0]) - 1, 0
        while start < end:
            mid = ((start + end) >> 1) + 1
            if "1" in [row[mid] for row in image]:
                start = mid
            else:
                end = mid - 1
        right = start

        area = (down - up + 1) * (right - left + 1)

        return area


if __name__ == '__main__':
    s = Solution()
    s.minArea(["0010", "0110", "0100"], 0, 2)
