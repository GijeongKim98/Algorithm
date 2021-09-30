class node:
    def __init__(self,key=None):
        self.key = key

class Dict:
    def __init__(self):
        Dict.a = []

    def binarySearch(self , search_key) :
        n = len(Dict.a)
        left = 0
        right = n-1

        while right >= left:
            half = (left + right) //2
            if Dict.a[half].key == search_key:
                return half
            if Dict.a[half].key > search_key:
                right = half - 1
            else:
                left = half + 1
            
        return -1

    
    def insert(self, v):
        Dict.a.append(node(v))
    

import random, time

N = 300000

key = list(range(1,N+1))
s_key = list(range(1,N+1))

random.shuffle(s_key)

d=Dict()

for i in range(N):
    d.insert(key[i])

start_time = time.time()

for i in range(N):
    result = d.binarySearch(s_key[i])
    if result == -1 or key[result] != s_key[i]:
        print('탐색오류')

end_time = time.time() - start_time
print("이진탐색 실행 시간 (N=%d) : %0.3f"%(N, end_time))
print('탐색완료')