n = int(input())

result = [0] * 1002
result[1] = 1
result[2] = 3

for i in range(3,n+1):
    result[i]=result[i-1]+result[i-2]*2

print(result[n]%10007)