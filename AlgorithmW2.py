#알고리즘 2주차

#binarySearch

def binarySearch(a, key, left, right) :
    
    if(left <= right):
        mid = (left + right) // 2
        # print('key = ', key, ', mid = ', mid, ', left = ', left, ', right = ', right )
        if (key == a[mid]) :
            print('key = ', key, ', mid = ', mid)
            return mid
        elif (key < mid) :
            print('key = ', key, ', mid = ', mid, ', left = ', left, ', right = ', mid-1 )
            return binarySearch(a, key , left, mid-1)
        else :
            print('key = ', key, ', mid = ', mid, ', left = ', mid+1, ', right = ', right )
            return binarySearch(a, key , mid+1, right)
    else :
        return -1

Arr = range(100)
key = 45
if binarySearch(Arr, key, 1, len(Arr)):
    print (key)
else :
    print('찾지못했습니다.')

