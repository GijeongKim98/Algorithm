def boubleSort(a,n) :
    for i in range(n,1,-1): #[n,n-1,...,2]
        for j in range(1,i): # [1,2,3,..,i-1]
            if(a[j]>a[j+1]):
                a[j+1], a[j] = a[j], a[j+1]


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

boubleSort(b, N)

end_time = time.time() - start_time

print("버블 정렬의 실행 시간 (N=%d, 정렬배열) : %0.3f"%(N, end_time))
checkSort(b,N)