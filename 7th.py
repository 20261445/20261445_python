'''
aa = [0,0,0,0,0,0,0,0,0,0]
hap = 0

aa[0] = int(input("첫 번째 숫자: "))
aa[1] = int(input("두 번째 숫자: "))
aa[2] = int(input("세 번째 숫자: "))
aa[3] = int(input("네 번째 숫자: "))
aa[4] = int(input("다섯 번째 숫자: "))
aa[5] = int(input("여섯 번째 숫자: "))
aa[6] = int(input("일곱 번째 숫자: "))
aa[7] = int(input("여덟 번째 숫자: "))
aa[8] = int(input("아홉 번째 숫자: "))
aa[9] = int(input("열 번째 숫자: "))

hap = aa[0] + aa[1] + aa[2] + aa[3] + aa[4] + aa[5] + aa[6] + aa[7] + aa[8] + aa[9]

print("\n 합계: %d" % hap)


bb = []
cc = []
value = 0

for i in range(0, 200):
    bb.append(value)
    value += 2

for i in range(0, 200):
    cc.append(bb[199 - i])

print("\n bb[0]에는 %d이, bb[199]에는 %d이 입력됩니다." % (bb[0], bb[199]))
'''


myList = [30, 10, 20]
print("현재 리스트 : %s" % myList)

myList.append(40)
print("append(40) 후 리스트 : %s" % myList)

print("pop() 으로 추출한 값 : %s" % myList.pop())
print("pop() 후 리스트 : %s" % myList)

myList.sort()
print("sort() 후 리스트 : %s" % myList)

myList.reverse()
print("reverse() 후 리스트 : %s" % myList)

print("20값의 위치 : %d" % myList.index(20))

myList.insert(2, 222)
print("insert(2, 222) 후 리스트 : %s" % myList)

myList.remove(222)
print("remove(222) 후 리스트 : %s" % myList)

myList.extend([77, 88, 77])
print("extend([77, 88, 77]) 후 리스트 : %s" % myList)

print("77값의 개수 : %d" % myList.count(77))


list1 = []
list2 = []
value = 0

for i in range(0, 4):
    for k in range(0, 5):
        list1.append(value)
        value += 3
    list2.append(list1)
    list1 = []


for i in range(0, 4):
    for k in range(0, 5):
        print("%2d" % list2[i][k], end=" ")
    print("")


ss = 'Python is Easy. 그래서 programming이 재미있습니다. ^^'
print(ss.upper())
print(ss.lower())
print(ss.swapcase())
print(ss.title())


inStr = " 한글 Python 프로그래밍 "
outStr = ""

for i in range(0, len(inStr)):
    if inStr[i] != ' ':
        outStr += inStr[i]

print("공백 제거 전 문자열 ==>" + '[' + inStr + ']')
print("공백 제거 후 문자열 ==>" + '[' + outStr + ']')


inStr = " <<<파<<이>>썬>>> "
outStr = ""

for i in range(0, len(inStr)):
    if inStr[i] != '<' and inStr[i] != '>':
        outStr += inStr[i]

print("< > 제거 전 문자열 ==>" + '[' + inStr + ']')
print("< > 제거 후 문자열 ==>" + '[' + outStr + ']')

