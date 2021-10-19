'''
x = 3
print (x)
x = -10 
print (x)

x = x + 10 
print (x)


print (li) 

print(li[2])
print(li[-2])
print(li[-2][2])

new = li[2:-3]
print(new)


ln = [1,3,-100]
ls = ['python', 'z', 'a', 'math', 'inu']
print (ln + ls)
print(ln*3)


#len == length of list : len(list)
li = ['python', -5 , 0,[0,1,2] ,3 ]
print (len(ln)) # 길이를 알려주는 함수 
print (type(ls[1])) # 타입을 알려주는 함수 

print(ln[1])
ln[1] = 1000
print(ln[1])
# 리스트의 인덱스에 해당하는 값을 바꿀 수 있음 string은 못바꿈

#list function
# add element to list : list.append(element) // string은 불가능
ln.append(10000)
print(ln)
# delete element from list : del list[index]
# delete range of elements from list 
    # del list[start:end]
del ln[1]
print(ln) # 1000이 사라짐
print(ln[1])
del li[2:4]
print (li)


# quiz
ls2 = [100,0]
print (ls)
#ls.append(ls2)
#print (ls)  
print (ls + ls2)

# list.sort() // 크기순으로 정렬
# list.reverse() // 거꾸로 정렬
# list.pop(index) // 인덱스 값을 빼버림
# list.count(element) // 몇개 들어갔는지 체크
# list.extend(list2) is same as list + list2


a = 1 # a is 1
b = a # b is 1   assigns value of a to b // a의 값을 b에 지정
print(a)
print(b)
a = 100
print(a)
print(b)

x = [1,2,3]
y = x  #assigns address of x to y
print (x)
print (y)

x[0] = 100 # x = [100,2,3]
print(x)
print(y)  #값이 같이 변하는 것을 알수 있음 같은 곳을 가리키고 있음

#id(element) : returns memory address of element 씨에서 포인터 
print (id(a))
print (id(b))


print (id(x))
print (id(y)) # 두개의 주소가 동일함  

x = [1,2,3]
y = x[:]  # y = [1,2,3]과 동일
print (id(x))
print (id(y))

# list slicing을 하면 다른 리스트에 바꿀수 있다
x[0] = 100
print (y)

# Boolean : true or false 
x = True
y = False
print (x)
print (y)
# Boolean operations : not, and, or
z = not x
w = not y
print (z)
print (w)
z = x and y # z is True if and only if both x and y are True
print(z)
z = x or y # z is True if and only if either x or y is True

a = x and (y or w) and not z
print (a)  # homework , why False? 

# relational operations:
s = 100
t = 10
b = (s == t) #  == : equality comparison  // 괄호 생략가능 연산자 우선순위에 의해
print (b)
#size comparison  : < , > , <=, => 
b = (s < t)
print (b) 
c = (s > t)
print (c)
# (!=)not equality comparison
d = (s != t)
print(d)

# (a == b) == True if and only if (a != b) == False
# (a >= b) == True if and only if (a == b) or a>b == True 

list1 = [1,2,3]
list2 = list1[:]
list3 = list1
print(list1)
print(list2)
print(list3)

 # == : equqlity comparison 
print (list1 == list2) # True
print (list2 == list3) # True
print (list3 == list1) # True

print(id(list1))
print(id(list2))
print(id(list3))

# is : compares memory address

print (list1 is list2)  # False
print (list2 is list3)  # False 
print (list3 is list1)  # True

# all variables are either True or False
x = 0
print (type (x))
print (type (True))
print (x == True)
print (x == False)

# True : 1, non-empty string, non-empty list
# False : 0 , empty string, empty list



# cnditional statement
# if statement :
#           something  <---- indentation is important
# usually, indentation is done by either tab or four whitespaces

x = 7
print (x)
if x % 2 == 0 :  ##
    print('even number')  # tab키 가 없으면 에러 발생 // indentation ERROR
    print('not an odd number')## if statement
if x % 2 == 1 :  ##
    print ('odd number') 
    print ('not an even number')## if statement

# if - else statement
# if boolean:
#       something
# else :  // if boolean if false, then execute
#       something

if x % 2 == 0:
    print('even number')
else : 
    print('odd number')

y = 100
if y % 4 == 0:
    print('remainder is 0')
else : # otherwise 1,2,3
    if y % 4 == 1:
        print('remainder is 1')
    else : # otherwise 2,3
        if y % 4 == 2:
            print('remainder is 2')
        else : # otherwise 3
            print ('remainder is 3')

# if - else if - else statement
# if boolean :
#       something
# elif boolean :
#       something
# else :
#       something

if y % 4 == 0:
    print('remainder is 0')
elif y % 4 == 1: # otherwise 1,2,3
    print('remainder is 1')
elif y % 4 == 2: # otherwise 2,3
    print('remainder is 2')
else : # otherwise 3
    print ('remainder is 3')

# coding philosophy  -- else is meant for error checking!
# pass : do nothing in that case

if y % 4 == 0:
    pass
    # print('remainder is 0')
elif y % 4 == 1: # otherwise 1,2,3
    print('remainder is 1')
elif y % 4 == 2: # otherwise 2,3
    print('remainder is 2')
elif y % 4 == 3: # otherwise 3
    print('remainder is 3')
else : # error checking!
    print ('something is wrong, error!')


# looping statements
# while - loop
# while boolean:
#       something  <--- executed if boolean is True
#                  <--- indentation is important!!
# 1. check boolean, if true then go to 2.
# 2. execute something, then go to 1.


# task : print numbers from 1 to 10
i = 1
while i < 11 :
    print (i, end = "  ")
    i = i + 1 
print('')
# task : print elements in list
li = [1, 2, 'inu', 'math']
print (li)

i = 0
while (i < len(li)):
    print (li[i])
    i = i + 1


# for - loop
# for variable in list:
#       something <--- indentation is important!
# 
# 1. for each element in list , execute something

for x in li:
    print (x)

for i in range(10) : # range(i) == [0,1,2,3, ... , i-1]
    print (li[i])
    # error code  index가 4 가 될수 없음

for i in range( len(li) ) : 
    print (li[i])  

s = 'inu math'
print (s.find('u'))
print (s.find('x'))

# terminal statement
# break -- end loop
# continue -- ignore rest of iteration of loop

# task - print index of element
li = [4, 6, -3, -10, 4]
for x in li:
    if x == 6 :
        print(True)
        break
    else :
        print(False)

# task - print frequency of element
i = 0
for x in li:
    print (x)
    if x != 4:
        print('entered continue')
        continue
    i = i + 1
    print ('increased i')
print (i)

# defining functions
# def functionName(parameters):
#       something  <---- indentation is important
def intro():
    return 'hello Python World'
print (intro())

print ('a' * 100)

def printA(n):
    return print ('a' * n)

printA(10) #same as print('a' * 10)

def printS(s,n):
    return print(s * n)

printS('inu', 10) # same as print('inu' * 10)

#sum of first 10 numbers
sum = 0
li = [1,2,3,4,5,6,7,8,9,10]
for x in li:
    sum = x + sum
print(sum)

def sumNum(n) :
    s = 0
    for x in range(n + 1):
        s = x + s
    return print (s)

sumNum(100) 


# default values for function
def printS(s, n):
    return print(s * n)
printS('inu', 10)
printS('math', 5)
# printS('python') ---- error code ,  
# 기본값을 넣을 수 있음
def printS1(s, n = 1):
    return print(s * n)
printS1('python')


# scope - world where each variable lives


def test(a): # this a is same as
    a = 100  # this a
a = 1        # this a is different from a in changeA
print (a)
test(a)
print(a) 

def realChangeA():
    return 100
a = 1
a = realChangeA()
print(a)
'''

# Algorithm : a list of produces to accomplish a given tesk

# 명령어들의 나열
    # each algorithm has as input and output  
    # 하나의 블랙박스 : input --> [algorithm]  ---> output

# good Algorithm ? 
    # time and space(memory, resource) : 시간복잡도, 공간복잡도 
        #accomplish task faster
    # scalablity : asymptotic analysis : 러닝타임이 얼마나 빠른가 (입력size에 고려)


# complex multiplication 
    # input : [ a,b,c,d ] -> output : [ac - bd, bc + ad]
    # more algorithm : a,b,c,d -> compute [a*c , b*d , b*c, a*d] ... 4 multiplication
    #                          -> compute [ac - bd, bc + ad] ... 2 addition 
    # better algorithm : a,b,c,d  -> (a+b)(c+d) = ab + ad + bc + bd
    #                             -> bc + ad = (a+b)(c+d) - ac - bd 
    #                             result : 3 multiplication , 5 addition

# computing powers : a^n
    # input : non negative integer a and n
    # output : compute a^n
    # 안좋은 방법 : multiply a , n times , -> n^(-1) multiplication
    # better algorithm : a^n  = a^(n/2_) * a^(n/2^^) = {a^(n/2_)}^2 * a or 1 
    #                                        => log_3 n multiplication
    # 

# SORTING   : [2,4,1,3,5] -> [1,2,3,4,5]
    #   input : list
    #   output : sorted list
    #   bubble, selection, insertion, merge, quick


a = [1]
p  = (a[3] == None)
print(p)
