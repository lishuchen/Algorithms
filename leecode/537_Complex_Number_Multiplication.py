#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a and not b:
            return None

        split = a.index('+')
        a_real = int(a[:split])
        a_cmplx = int(a[split + 1: -1])

        split = b.index('+')
        b_real = int(b[:split])
        b_cmplx = int(b[split + 1: -1])

        rsl_real = a_real * b_real - (a_cmplx * b_cmplx)
        rsl_cmplx = a_real * b_cmplx + a_cmplx * b_real

        return str(rsl_real) + "+" + str(rsl_cmplx) + "i"
