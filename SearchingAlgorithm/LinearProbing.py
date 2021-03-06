class Dict:
    def __init__(self):
        Dict.a = [-1] * M
    
    def search(self, v):
        x = self.hash(v)
        while Dict.a[x] != -1:
            if v == Dict.a[x]:
                return Dict.a[x]
            else:
                x = (x-1) % M
        return -1
    
    def insert(self,v):
        x = self.hash(v)
        while Dict.a[x] != -1:
            x = (x+1) % M
        Dict.a[x] = v

    def hash(self,v):
        return v % M

    def print(self):
        for i in range(M):
            if Dict.a[i] != -1:
                print('#', end = '')
            else:
                print(' ', end = '')
            if (i+1) % 60 == 0:
                print()

import random, time

N = 10000
M = 10391
# N = 1000
# M = 1009
key = []
s_key = []