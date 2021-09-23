def merge(a,l,m,r):
    i = l
    j = m+1
    k = l
    b = a.copy()

    while i <= m and j <= r :

        if a[i] < a[j] :
            b[k] = a[i]
            i += 1
            k += 1

        else :
            b[k] = a[j]
            j += 1
            k += 1

    if i > m :
        for n in range(j,r+1):
            b[k] = a[n]
            k = k+1

    else :
        for n in range(i,m+1):
            b[k] = a[n]
            k = k + 1

    a = b.copy()
    print(a)

    # b =a.copy()



def mergeSort(a,l,r):
    #배열 a[]부분 배열 a[l:r]을 오름 차순 정렬
    #print("-----------------------------------------------")
    if  r > l:
        m = (r+l) // 2
        mergeSort(a,l,m)
        mergeSort(a,m+1,r)
        merge(a,l,m,r)


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

N = 1000

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

mergeSort(a, 1, N)

end_time = time.time() - start_time

print("합병정렬의 실행 시간 (N=%d, 랜덤배열) : %0.3f"%(N, end_time))
checkSort(a,N)