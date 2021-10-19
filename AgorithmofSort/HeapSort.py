def heapify(a,h,m):
    v = a[h]
    j = 2 * h

    while j <= m :

        if j < m and a[j] < a[j+1]:
            j += 1

        if v >= a[j]:
            break

        else :
            a[j//2] = a[j]

        j *= 2

    a[j//2] = v

def heapSort(a ,n) :

    for i in range(n//2,0,-1):
        heapify(a,i,n)

    for i in range(n-1,0,-1):
        a[1], a[i+1] = a[i+1], a[1]
        heapify(a,1,i)
    

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


a.append(None) # a[0]의 값 더미키
b.append(None) # b[0]의 값 더미키
c.append(None) # c[0]의 값 더미키

for i in range(N):

    a.append(random.randint(1, N))
    b.append(i+1)
    c.append(N-i)

start_time = time.time()

heapSort(a, N)

end_time = time.time() - start_time

print("히프정렬의 실행 시간 (N=%d, 역순배열) : %0.3f"%(N, end_time))
checkSort(a,N)