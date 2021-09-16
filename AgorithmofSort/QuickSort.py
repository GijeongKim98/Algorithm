
def partition(a,l,r):
    #print(a)
    
    v = a[r]
    i = l - 1
    j = r

    while True:
        i = i + 1 
        while a[i] < v:
            i = i + 1

        j = j - 1 
        while a[j] > v:
            j = j - 1

        if i > j :
            break
        
        a[i], a[j]=a[j], a[i]
        #print(a)

    a[i] , a[r] = a[r] ,a[i]
    #print(a)
    return i



def quickSort(a,l,r):
    #배열 a[]부분 배열 a[l:r]을 오름 차순 정렬
    #print("-----------------------------------------------")
    if  r > l:
        i = partition(a,l,r)
        quickSort(a,l,i-1)
        quickSort(a,i+1,r)
    

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


a.append(-1) # a[0]의 값 더미키
b.append(-1) # b[0]의 값 더미키
c.append(-1) # c[0]의 값 더미키

for i in range(N):

    a.append(random.randint(1, N))
    b.append(i+1)
    c.append(N-i)

start_time = time.time()

quickSort(c, 1, N)

end_time = time.time() - start_time

print("퀵정렬의 실행 시간 (N=%d, 정렬배열) : %0.3f"%(N, end_time))
checkSort(c,N)