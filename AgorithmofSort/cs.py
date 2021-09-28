a = [0,1,2,2,1,3,4,4,1]
b = [0,0,0,0,0,0,0,0,0]

count = []
count.append(0)
for k in range(1,5):
    count.append(0)

for i in range(1,9): # 9는 N+1의 값을 의미
    count[a[i]] += 1
    

for i in range(1,5):  # 5는 k+1의 값을 의미
    count[i] += count[i-1]

print (count)

for i in range(8,0,-1):
    b[count[a[i]]] = a[i]
    count[a[i]] -= 1
    
print(b)