
##############################최소히프클래스구축#################################
class PQ:
    def __init__(self):
        self.heap = [0]*100
        self.info = [0]*100
        self.n = 0

    def insert(self, v, x):  #  v : count[i], x : i // count를 기준으로 히프구조 만들기
        self.n += 1
        i = self.n
        while True:
            if i == 1: break
            if v >= self.heap[int(i/2)]:break
            self.heap[i] = self.heap[int(i/2)]
            self.info[i] = self.info[int(i/2)]
            i = int(i/2)
        self.heap[i] = v
        self.info[i] = x

    def remove(self):
        x = self.info[1]
        temp_v = self.heap[self.n]
        temp_x = self.info[self.n]
        self.n -= 1
        i = 1
        j = 2
        while j <= self.n:
            if (j < self.n) and (self.heap[j] > self.heap[j+1]):
                j += 1
            if temp_v <= self.heap[j]: break
            self.heap[i] = self.heap[j]
            self.info[i] = self.info[j]
            i = j
            j *= 2
        self.heap[i] = temp_v
        self.info[i] = temp_x
        return x

    def isEmpty(self):
        if self.n == 0: return True
        else: return False
############################################################################


#############################아스키코드변환합수###############################
# 아스키코드는 공백 : 32 // 알파벳대문자 : 65 ~ 90
def index(c):
    if ord(c) == 32: return 0  # 아스키코드 변황(ocd)
    else: return (ord(c)-64)
# 변환후 공백  A B C ...
       #  0   1 2 3 ...
###########################################################################


###########################허프만코드생성함수###############################
def makeHuffman(t, m):

    ###### < 문제1-1(count 만들고 출력하기) > #######
    for i in range(m):
        count[index(t[i])] += 1
    print("count : ", count[:27])
    ################################################
    
    
    ## 최소히프에 값 추가하기(조건 : count[i] > 0) ##
    for i in range(27):
        if count[i]:
            pq.insert(count[i], i)
    ################################################



    ###### < 문제 1-2: dad와 count 출력하기 >  #######
    ##### 최소히프에서 제거하면서 dad값 구하기 #######
    i = 27
    while not pq.isEmpty():
        t1 = pq.remove()
        t2 = pq.remove()
        dad[i] = 0
        dad[t1] = i
        dad[t2] = -i
        count[i] = count[t1] + count[t2]
        if not pq.isEmpty(): 
            pq.insert(count[i], i)
        i += 1
    print("count : ",count[:44])
    print("dad : ",dad[:44])
    ################################################
    ################################################

    ###################### < 문제1-3 > ######################
    ########### code[]와 length[]구축하고 출력하기 ###########
    for k in range(27):
        i = x = 0
        j = 1
        if count[k]:
            q = dad[k]
            while q:
                if q < 0:
                    x += j
                    q = -q
                q = dad[q]
                j += j
                i += 1
        code[k] = x
        length[k] = i
        code0 = '' 
        while i > 0:
            code0 += str((x >> i - 1) & 1)
            i -= 1
        if k == 0:
            print("   // ","length : ",length[k] ," // ","code : ", code0)
        else:
            print(chr(k+64)," // ","length : ",length[k] ," // ","code : ", code0)

    ###########################################################
    ###########################################################

#############################################################################


############################### < encode함수 > ###############################
def encode(t, m):
    huffman_code = ''
    for j in range(m):
        i = length[index(t[j])]
        while i > 0:
            huffman_code += str((code[index(t[j])] >> i - 1) & 1)
            i -= 1
    return huffman_code
###########################################################################


############################### < decode함수 > ###############################
# dad[i] = 0인것이 많았지만 초기의 설정에서 텍스트에 해당문자가 들어가지 않는경우 -1을 부여하였습니다.
# 그것을 이용해 dad배열에서 0이 가장큰 인덱스의 값입니다.
############################### < decode함수 > ###############################
# dad[i] = 0인것이 많았지만 초기의 설정에서 텍스트에 해당문자가 들어가지 않는경우 -1을 부여하였습니다.
# 그것을 이용해 dad배열에서 0 인값이 가장큰 인덱스 값입니다.
##############################################################################
def decode(t):
    result = ''
    m = len(t)
    for i in range(100):
        if dad[i] == 0:
            maxindex = i 
            break
    # print(maxindex)
    i = 0
    while i < m:
        k = maxindex
        while k >= 26:
            if t[i] == '1': 
                k *= -1
            k = dad.index(k)
            i += 1

        if k == 0:
             result += ' '
        else:
            k += 64
            result += str(chr(k))
        
    return result
#############################################################################

text = 'A SIMPLE STRING TO BE ENCODED USING A MINIMAL NUMBER OF BITS'
count = [0]*100
dad = [-1]*100
length = [0]*27
code = [0]*27
M = len(text)
pq = PQ()
makeHuffman(text, M)
encodestr = encode(text, M)
print(encodestr)
decodestr = decode(encodestr)
print(decodestr)