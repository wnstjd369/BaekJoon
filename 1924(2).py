# 갤랜더 모듈이 있다고 한다.
import calendar
m , d = map(int,input().split())
week = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
day = calendar.weekday(2007,m,d)

print(week[day])
