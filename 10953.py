N = int(input())
num_list = list()
for i in range(N):
    a , b = map(int,input().split(','))
    num_list.append((a,b))

for i in num_list:
    print(i[0]+i[1])