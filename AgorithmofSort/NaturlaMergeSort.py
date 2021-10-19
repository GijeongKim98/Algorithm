
def merge(a,l,m,r):
    i = l
    j = m+1
   # print('j = ', j )
    k = l
    

    # print("b = ",b)

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
            k = k + 1
            # print(b)

    else :
        for n in range(i,m+1):
            b[k] = a[n]
            k = k + 1
            # print(b)

    for p in range(l,r+1):
        a[p] = b[p]
    # print("a = ",a)

def searchingrun (a,n):
    indexl = [1]
    for i in range(1,n):
        if a[i] > a[i+1]:
            indexl.append(i+1)
 #   print(b)
    return indexl


def naturalMergeSort(a,n):  
    indexList = searchingrun(a,n)
    k = len(indexList)
    indexList.append(-100)
#    print(k)
    cpList = []

    while (k > 1):
 #       print('k = ',k)
        for i in range(0,k,2):
  #          print(i)
            if indexList[i+1] == - 100:
                cpList.append(indexList[i])
            elif indexList[i+2] == -100:
                merge(a,indexList[i],indexList[i+1]-1,n)
                cpList.append(indexList[i]) 
            else:       
                merge(a,indexList[i],indexList[i+1]-1,indexList[i+2]-1)
                cpList.append(indexList[i])
        
        indexList = cpList
        cpList = []
        # print(indexList)
        k = len(indexList)
        indexList.append(-100)



##a = [None,6,7,8,3,4,1,5,9,10,2,17,18]
##naturalMergeSort(a,10)        

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
b1 = []
c = []


a.append(None) # a[0]의 값 
b1.append(None) # b[0]의 값 
c.append(None) # c[0]의 값 

for i in range(N):

    a.append(random.randint(1, N))
    b1.append(i+1)
    c.append(N-i)


b = a.copy()
start_time = time.time()

naturalMergeSort(a, N)

end_time = time.time() - start_time

print("자연합병정렬의 실행 시간 (N=%d, 랜덤배열) : %0.3f"%(N, end_time))
checkSort(a,N)