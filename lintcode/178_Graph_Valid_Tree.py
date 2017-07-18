class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here
        if len(edges) < n - 1:
            return False

        self.lst = list(range(n))
        for a, b in edges:
            root_a = self.find(a)
            root_b = self.find(b)
            if root_a == root_b:
                return False
            else:
                self.lst[root_a] = root_b

        return True

    def find(self, a):
        while self.lst[a] != a:
            a = self.lst[a]

        return a
