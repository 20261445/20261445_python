# '''
# for i in range(0, 3 ,1):
#     print("안녕하세요? for 문을 공부 중입니다.")
#     ## i 대신 "_" 사용 가능 ##

# for i in range(1, 6 ,1):
#     print("%d" %i, end=" ")



# for i in range(1, 101, 2):
#     print("%d" % i, end=" ")

# for i in range(2, 101, 2):
#     print("%d" % i, end=" ")


# i, hap = 0, 0

# for i in range(1, 11, 1):
#     hap += i

# print("\n 1부터 10까지의 합: %d" % hap)
# '''

# '''
# hap = 0

# for i in range(1, 101, 2):
#     hap += i

# print("\n 1부터 100까지 홀수의 합: %d" % hap)

# hap = 0

# for i in range(2, 101, 2):
#     hap += i

# print("\n 1부터 100까지 짝수의 합: %d" % hap)


# i, dan = 0, 0

# dan = int(input("\n 단을 입력하세요: "))

# for i in range(1, 10, 1):
#     print("%d * %d = %2d" % (dan, i, dan * i))


# for i in range(0, 3, 1):
#     for k in range(0, 2, 1):
#         print("파이썬은 꿀잼입니다. ^^(i값 : %d, k값 : %d)" % (i, k))
# '''



# # 구구단을 옆으로 출력
# for i in range(9, 1, -1):
#     print("## %d단 ##" % i, end="\t")
# print()

# for k in range(9, 0, -1):
#     for i in range(9, 1, -1):
#         print("%d * %d = %2d" % (i, k, i * k), end="\t")
#     print()


# for i in range(2, 10, 1):
#     print("## %d단 ##" % i, end="\t")
# print()

# for k in range(1, 10, 1):
#     for i in range(2, 10, 1):
#         print("%d * %d = %2d" % (i, k, i * k), end="\t")
#     print()


# i, hap = 0, 0

# i = 1
# while i < 11:
#     hap += i
#     i += 1

# print("\n 1부터 10까지의 합계: %d" % hap)

# '''
# while True:
#     print("ㅋ", end=" ")
# '''

# hap = 0
# a, b = 0, 0

# while True :
#     a=int(input("\n 더할 첫 번째 수를 입력하세요: "))
#     if a == 0 :
#         break
#     b=int(input(" 더할 두 번째 수를 입력하세요: "))
#     hap = a + b
#     print("\n %d + %d = %d" % (a, b, hap))

# print("\n 0을 입력해 반복문을 탈출했습니다.")


# hap, i = 0, 0

# for i in range(1, 101):
#     if i % 3 == 0:
#         continue

#     hap += i

# print("\n 1부터 100까지의 수 중 3의 배수를 제외한 합계: %d" % hap)


# i, k, guguLine = 0, 0, ""

# for i in range(2, 10):
#     guguLine = guguLine + ("# %d단 #" % i)

# print(guguLine)

# for i in range(1, 10):
#     guguLine = ""
#     for k in range(2, 10):
#         guguLine = guguLine + str("%2dX  %2d = %2d" % (i, k, i * k))
#     print(guguLine)

for i in range(1, 51):
    print("*" * i)
print("-" * 51)

for i in range(49, 0, -2):
    print(" " * ((51 - i) // 2) + "*" * i)

for i in range(3, 51 , 2):
    print(" " * ((51 - i) // 2) + "*" * i)
