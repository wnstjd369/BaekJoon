N = int(input())
# 결과 배열 생성
result = [0]*1000001

# 2와 3인 경우는 딱 나누어 떨여져 1이므로 따로 넣어줬다.
for i in range(2,4):
    result[i] = 1

# 4부터 시작.
for i in range(4,N+1):
    # 일단 현재 값에서 1뺴고 result[i] 에 넣어본다.
    result[i]=result[i-1] +1
    #만약 3의 배수인 경우에 3으로 나누는게 더 작은지, 아니면 그냥 -1했을떄가 더 작은지 비교해서 더 작은값을 넣어준다.
    if i%3 == 0:
        result[i] = min(result[i//3]+1,result[i])
    # 3으로 나눴든 1을 뺸게 result[i]에 있던간에 그 값과 2로 나눴을떄의 값과 비교해 어느게 떠 빨리 1로 만드는지 비교해여 result[i]에 넣어준다.
    if i%2 == 0:
        result[i] = min(result[i//2]+1,result[i])

# 입력한 N까지 차례로 그 숫자까지 걸리는 최소횟수가 들어가있다 N번쨰를 출력한다.
print(result[N])
