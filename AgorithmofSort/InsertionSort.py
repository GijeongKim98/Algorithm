def insertionSort(a,n):
    for i in range(2,n+1):
        v = a[i]
        j = i
        while(a[j-1] > v):
            a[j] = a[j-1]
            j = j - 1
        a[j] = v

    

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

N = 15000

a = []
b = []
c = []

a.append(-1) # a[0]의 값 더미키
b.append(-1) # b[0]의 값 더미키
c.append(-1) # c[0]의 값 더미키

for i in range(N):

    a.append(random.randint(1, N))
    b.append(i+1)
    c.append(N-i)

start_time = time.time()

insertionSort(c, N)

end_time = time.time() - start_time

print("삽입정렬의 실행 시간 (N=%d, 역순배열) : %0.3f"%(N, end_time))
checkSort(c,N)