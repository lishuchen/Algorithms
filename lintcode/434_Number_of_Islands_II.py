# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {int} n an integer
    # @param {int} m an integer
    # @param {Pint[]} operators an array of point
    # @return {int[]} an integer array
    def numIslands2(self, n, m, operators):
        # Write your code here
        if not operators:
            return []

        self.n = n
        self.m = m
        self.map = [[0] * m for _ in range(n)]
        self.uf = list(range(n * m))
        rsl = list()
        counter = 0
        for pt in operators:
            if self.map[pt.x][pt.y] != 1:
                self.map[pt.x][pt.y] = 1
                counter -= self.search(pt.x, pt.y)
            rsl.append(counter)

        return rsl

    def transform(self, i, j):
        return i * self.m + j

    def find(self, i, j):
        root = self.transform(i, j)
        while self.uf[root] != root:
            root = self.uf[root]

        return root

    def search(self, x, y):
        index = self.transform(x, y)
        count = 0
        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + i, y + j
            if -1 < new_x < self.n and -1 < new_y < self.m and self.map[new_x][new_y] == 1:
                root_n = self.find(new_x, new_y)
                if root_n != index:
                    self.uf[root_n] = index
                    count += 1

        return count - 1
