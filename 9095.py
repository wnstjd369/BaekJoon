# 123 더하기
# 정수 n이 주어졌을떄 n을 1 2 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오

# 첫줄에 테스트 케이스 T가 주어진다.
T = int(input())
# 정수 n이 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있고 정수 N은 양수이며 11보다 작다.

arr = list()
for a in range(T):
    n = int(input())
    result = [0] * (11)

    result[1] = 1
    result[2] = 2
    result[3] = 4

    for i in range(4,n+1):
        result[i] = result[i-1]+result[i-2]+result[i-3]

    arr.append(result[n])

for b in arr:
    print(b)