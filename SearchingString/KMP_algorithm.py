def initNext(p):
    next = []
    for i in range(len(p)) :
        next.append(0)
    M = len(p)
    next[0] = -1
    i = 0
    j = -1
    while (i < M):
        if j != -1 and p[i] == p[j] :
            next[i] = next[j]
        else:
            next[i] = j 
        while (j>=0 and p[i] != p[j]):
            j = next[j]
        i += 1
        j += 1
    return next

def KMP(p,t):
    count = 0
    indexlist = []
    M = len(p) - 1
    N = len(t)
    next = initNext(p)

    i = 0 
    j = 0
    while i < N:
        count += 1
        while j >= 0 and t[i] != p[j]:
            j = next[j]
        if j == M:
            indexlist.append(i-M)
            j = -1
        j += 1
        i += 1
    print("비교횟수 : ", count)
    return indexlist
            
t = 'ababacabcbababcacacbcaababca\0'
p = 'ababca'
ilist = KMP(p,t)
if len(ilist) > 0 :
    print('패턴시작위치 :', ilist)
else :
    print("해당 패턴을 찾지못했습니다.")