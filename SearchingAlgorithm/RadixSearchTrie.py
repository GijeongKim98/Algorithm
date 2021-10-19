class bitskey:
    def __init__(self,x):
        self.x = x
    
    def get(self):
        return self.x

    def bits(self, k, j):
        return (self.x >> k) & ~(~0 << j)
    
class node:
    def __init__(self, key):
        if key.get() == 0:
            self.key = bitskey(0)
            self.external = False
        else :
            self.key = key
            self.external = True

        self.right = 0
        self.left = 0


class Dict:
    itemMin = bitskey(0)
    head = 0
    head_check = False

    def search(self,v):
        v = bitskey(v)
        return self.searchR(self.head, v, maxb - 1)

    def insert(self,v):
        v = bitskey(v)
        return self.insertR(self.head, v, maxb - 1)

    def insertR(self, h, v, d):
        if h == 0:
            h = node(v)
            if self.head_check == False:
                self.head = h
            return h
        if h.external:
            leaf = node(v)
            h = self.split(leaf,h,d)
            if self.head_check == False:
                self.head = h
                self.head_check = True
            return h
        if v.bits(d,1) == 0:
            pass
        # 아직 미완성

    