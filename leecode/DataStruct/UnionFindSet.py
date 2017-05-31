#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class UnionFind:
    def __init__(self):
        self.nodes = dict()

    def add(self, item, parent):
        if item not in self.nodes:
            self.nodes[item] = parent
        else:
            print("Duplicate item:", item)

    def union(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)
        if p_x != p_y:
            self.nodes[p_x] = p_y

    def find(self, item):
        '''
        Compressed find
        '''
        if item not in self.nodes:
            print("Cannot found item", item)
            return

        parent = item
        while parent != self.nodes[parent]:
            parent = self.nodes[parent]

        # Compress the path
        boss = parent
        next = item
        while boss != self.nodes[next]:
            tmp = self.nodes[next]
            self.nodes[next] = boss
            next = tmp

        return boss

    def print(self):
        print(self.nodes)


if __name__ == "__main__":
    unionfind = UnionFind()
    unionfind.add(1, 1)
    unionfind.add(2, 1)
    unionfind.add(3, 3)
    unionfind.add(4, 5)
    unionfind.add(5, 5)
    unionfind.print()
    print(unionfind.find(2))
    unionfind.union(1, 3)
    unionfind.print()
    print(unionfind.find(2))
    unionfind.print()
    unionfind.union(1, 5)
    unionfind.print()
    print(unionfind.find(1))
    unionfind.print()
    print(unionfind.find(2))
    unionfind.print()
    print(unionfind.find(6))
    unionfind.print()
