def countingSort(a,n,k):
   
    b = a.copy()
    count = []
    count.append(0)
    for j in range(1,k+1):
        count.append(0)

    for i in range(1,n+1): # 9는 N+1의 값을 의미
        count[a[i]] += 1
    

    for j in range(1,k+1):  # 5는 k+1의 값을 의미
        count[j] += count[j-1]

# print (count)

    for i in range(n,0,-1):
        b[count[a[i]]] = a[i]
        count[a[i]] -= 1

    for i in range(n+1):
        a[i] = b[i]

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

N = 300000

a = []


a.append(None) # a[0]의 값 

for i in range(N):

    a.append(random.randint(1, 1000))

start_time = time.time()

countingSort(a, N, 1000)

end_time = time.time() - start_time

print("계수정렬의 실행 시간 (N=%d, 랜덤배열) : %0.3f"%(N, end_time))
checkSort(a,N)