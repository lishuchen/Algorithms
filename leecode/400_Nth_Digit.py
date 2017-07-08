class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # adjust the index
        n -= 1
        digit = 1
        start = 10 ** (digit - 1)

        while n >= 9 * start * digit:
            n -= 9 * start * digit
            digit += 1
            start = 10 ** (digit - 1)

        return int(str(start + n / digit)[n % digit])
