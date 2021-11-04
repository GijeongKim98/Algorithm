def initNext(p):
    next = []
    print(len(p))
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

p1 = 'ababca'
p2 = 'abababca'
p3 = 'abcbabcbabc'
p4 = 'abracadabra'

n1 = initNext(p1)
print(p1)
print(n1)

n2 = initNext(p2)
print(p2)
print(n2)

n3 = initNext(p3)
print(p3)
print(n3)

n4 = initNext(p4)
print(p4)
print(n4)