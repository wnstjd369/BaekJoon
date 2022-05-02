# 내가 짠거.
str1 = list(input())
while True:
    try:
        for i in range(10):

            print(str1[i],end="")
        print("")
        str1 = str1[10:]
    except:
        break
# 남이 짯는데 맘에 든거.
# words = input()
# for i in range(len(words)):
#     print(words[i],end=("\n" if (i+1)%10==0 else ""))