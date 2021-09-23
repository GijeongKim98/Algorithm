def mergeSort(a,l,r):
    if  r > l:
        m = (r+l) // 2
        mergeSort(a,l,m)
        mergeSort(a,m+1,r)

        # 1. 복사 하기 b[]에 a[]를 복사 
        #    b에 인덱스 1 ~ m 까지 a에 똑같이 복사
        #    b에 인덱스 m 이후 a의 역순으로 복사
        #   -> 만약 a = [1,5,8,9,2,3,7,10]이면  b = [1,5,8,9,10,7,3,2] 이다
        for i in range(m+1,l,-1):
            b[i-1] = a[i-1]
        i -= 1
        for j in range(m,r):
            b[r+m-j] = a[j+1]
        j += 1
        # 2. a에 정렬된 값으로 다시 넣기
        #       b[i]와 b[j]를 비교 해서 작은 값을 넣음
        for k in range(l,r+1):
            if b[i] < b[j] :
                a[k] = b[i]
                i += 1
            else :
                a[k] = b[j]
                j -= 1
        

def checkSort(a, n):

    isSorted = True

    for i in range(1, n):

        if a[i] > a[i+1]:

            isSorted = False

        if not isSorted:

            break

    if isSorted:

        print("정렬 완료")

    else:

        print("정렬 오류 발생")



import random, time

N = 100000

a = []
b = []
c = []
d = [-1,6,2,8,1,3,9,4,5,10,7]


a.append(None) # a[0]의 값 
b.append(None) # b[0]의 값 
c.append(None) # c[0]의 값 

for i in range(N):

    a.append(random.randint(1, N))
    b.append(i+1)
    c.append(N-i)

start_time = time.time()

mergeSort(c, 1, N)

end_time = time.time() - start_time

print("합병정렬의 실행 시간 (N=%d, 역순배열) : %0.3f"%(N, end_time))
checkSort(c,N)