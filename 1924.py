# 달이랑 날짜 입력.
m , d = map(int,input().split())

#1월 1일이 월요일
months = [31,28,31,30,31,30,31,31,30,31,30,31]
week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
day = 0

for i in range(m-1):
    day += months[i]

day = (day+d) % 7

print(week[day])