N = int(input())
num_list = list()
for i in range(N):
    a , b = map(int,input().split())
    num_list.append(a+b)

for i in range(len(num_list)):
    print(f'Case #{i+1}: {num_list[i]}')