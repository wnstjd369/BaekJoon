N = int(input())
num_list = list()
for i in range(N):
    a , b = map(int,input().split())
    print(f'Case #{i+1}: {a} + {b} = {a+b}')