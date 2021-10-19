class bitskey:

    def __init__(self, x): # 생성자 

        self.x = x



    def get(self):  

        return self.x



    def bits(self, k, j):

        return (self.x >> k) & ~(~0 << j)


class node:
    def __init__(self,key):  # 노드의 생성자 
        self.key = bitskey(key)  # bitskey 클래스 의 인스턴스 변수 self.key
        self.left = None
        self.right = None

class Dict:
    itemMin = bitskey(0) # itemMin = bitskey 클래스의 인스턴스 변수(가장 작은 값 0)

    z = node(itemMin) # z는 노드의 생성자로 key값이 00000을 의미
    head = node(itemMin) # head 도 마찬가지
 
     # head는 노드 이므로 왼쪽 오른쪽 값을 지정
    head.left = z 
    head.right = z

    def search(self,v):
        v = bitskey(v)
        x = self.head.right
        b = maxb
        self.z.key = v
        while v.get() != x.key.get():
            b = b-1
            if v.bits(b,1):
                x = x.right
            else:
                x = x.left
        
        if x == self.z:
            return -1
        else:
            return x.key.get()
        

    def insert (self,v):
        v = bitskey(v)
        b = maxb - 1
        x = self.head.left
        p = self.head

        while x.key.get() != self.z.key.get():
            p = x
            if v.bits(b,1):
                x = x.right
            else:
                x = x.left
            b = b - 1
        x = node(self.itemMin)
        x.key = v
        x.left = self.z
        x.right = self.z

        if v.bits(b+1,1):
            p.right = x

        else:
            p.left = x

    def check (self,v):
        v = bitskey(v)
        b = maxb
        p = self.head
        x = self.head.left
       # print(type(x))

        while x.key.get() != v.get():
            b = b - 1
            p = x
            if b < 0 :
                print ("key = " , v.get() ,"에 대한 입력오류." )
                return
            if v.bits(b,1):
                x = x.right
            else:
                x = x.left
        if b == maxb:
            print("key = ", v.get(), " / parent = ", v.get())
        else:
            print("key = ", v.get(), " / parent = ", p.key.get())
        


import random, time


maxb = 5
a = Dict()
b = [1,19,5,18,3,26,9]
c = [1,3,5,9,18,19,26]

for i in b:
    a.insert(i)

for i in c:
    a.check(i)