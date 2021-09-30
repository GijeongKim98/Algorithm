
# class 객체, self를 무조건 써줘야하며 this와 동일한 의미를 지님
class node:
    def __init__(self,key=None):
        self.key = key

class Dict:
    def __init__(self):
        Dict.a = []

    def search(self,search_key):
        i = 0
        n = len(Dict.a)
        while i < n:
            if Dict.a[i].key == search_key :
                break
            i += 1
        if i == n : 
            return -1
        else :
            return i
    
    def insert(self, v):
        Dict.a.append(node(v))
    

import random, time

N = 9000

key = list(range(1,N+1))
s_key = list(range(1,N+1))

random.shuffle(key)
d=Dict()

for i in range(N):
    d.insert(key[i])

start_time = time.time()
for i in range(N):
    result = d.search(s_key[i])
    if result == -1 or key[result] != s_key[i]:
        print('탐색오류')

end_time = time.time() - start_time
print("순차탐색 실행 시간 (N=%d) : %0.3f"%(N, end_time))
print('탐색완료')