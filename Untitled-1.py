a = [None,2,1,123,256]

def mergeSort(a,l,r):
    if  r > l:
        m = (r+l) // 2
        mergeSort(a,l,m)
        print("a 왼쪽 =", a)
        mergeSort(a,m+1,r)
        print("a 오른쪽 =", a)
        
        b = a.copy()
    

        while i <= m and j <= r :
            print("b = ",b)

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
                print(b)

        else :
            for n in range(i,m+1):
                b[k] = a[n]
                k = k + 1
                print(b)

        a = b.copy()
        print("a = ",a)

mergeSort(a,1,4)
