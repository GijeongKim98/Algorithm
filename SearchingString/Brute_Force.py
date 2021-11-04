def buteForce(p,t):
    indexlist = []
    M = len(p) - 1
    N = len(t)
    
    print(M, N)
    i = 0
    j = 0
    count = 0
    while(i < N): 
        count +=1

        if t[i] != p[j]:
            i = i - j
            j = -1

        if j == M:   
            indexlist.append(i - M)
            j = -1

        j += 1
        i += 1
        
    print('비교횟수 : ', count)
    return indexlist


t = 'ababacabcbababcacacbcaababca\0'
p = 'ababca'

list = buteForce(p,t)
if len(list) > 0 :
    print('패턴시작위치 :', list)
else :
    print("해당 패턴을 찾지못했습니다.")




        
