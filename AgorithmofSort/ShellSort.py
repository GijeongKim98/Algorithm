def shellSort(a,n):
    h = 1
    while(h<n):
        h = 3*h +1
    while(h > 0):
        for i in range(h+1,n+1):
            v = a[i]
            j = i
            while(j>h and a[j-h] > v):
                a[j] = a[j-h]
                j = j - h
            a[j] = v
        h = h//3


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

N = 5000

a = []
b = []
c = []

a.append(None) # a[0]의 값을 None이라 함
b.append(None) # b[0]의 값을 None
c.append(None) # c[0]의 값을 None

for i in range(N):

    a.append(random.randint(1, N))
    b.append(i+1)
    c.append(N-i)

start_time = time.time()

shellSort(c, N)

end_time = time.time() - start_time

print("쉘정렬의 실행 시간 (N=%d, 역순배열) : %0.3f"%(N, end_time))
checkSort(c,N)