# 알고리즘 1주차

# 제 1장 알고리즘과 문제해결

# 최대공약수 알고리즘

def gcd(a,b) :
    i = 1
    while(i<a and i<b):
        if(a%i == 0 and b%i == 0) :
            g = i
        i = i + 1
    return g
A = int(input('a = '))
B = int(input('b = '))
# print ('최대공약수 = ',gcd(A ,B))


# 소수찾기 알고리즘
def isPrime(a):
    i = 2
    while (i <= a/2) :
        if(a % i == 0):
            print('소수가 아닙니다')
        i = i + 1
    print('소수입니다.')
isPrime(17)

# 완전수 찾기 알고리즘
def isPerfect(a):
    s = 0
    i = 1
    while(i <= a/2) :
        if(a%i == 0) :
            s = s+i
        i = i + 1
    if(s == a) : 
        return True
    else :
        return False

if isPerfect(28) : 
    print('완전수 입니다.')
else : print('완전수 아닙니다.')


def isPalindrome(s):
    i = 0 
    j = len(s) -1
    while (i < j) :
        if(s[i] != s[j]) :
            return False
        i += 1
        j -= 1
    return True

S = 'abccba'
if isPalindrome(S) :
    print('회문 0')
else :
    print('회문 x')

def eratos(a,n):
    a[1] = 0
    i = 2
    while(i<=n/2):
        j = 2
        while(i*j <= n):
            a[i*j] =0
            j += 1
        i += 1
    return a

N = int(input('숫자입력 :'))
A = list(range(N+1))
res = eratos(A,N)
for i in range(N+1):
    if(res[i]):
        print(res[i], end =' ')
        10
