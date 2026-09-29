a = 9
b = 2

'''
산술 연산자
a//b = 몫
a%b = 나머지
a**b = 제곱
'''

'''
대입 연산자
+= : a += 3 -> a = a + 3 => a = 12
-= : a -= 3 -> a = a - 3 => a = 6
*= : a *= 3 -> a = a * 3 => a = 27
/= : a /= 3 -> a = a / 3 => a = 3.0
//= : a //= 3 -> a = a // 3 => a = 3
%= : a %= 3 -> a = a % 3 => a = 0
**= : a **= 3 -> a = a ** 3 => a = 729
'''

'''
관계 연산자
a = 3, b = 9 일때,
a == b : a와 b가 같으면 True, 다르면 False -> False
a != b : a와 b가 다르면 True, 같으면 False -> True
a > b : a가 b보다 크면 True, 작으면 False -> False
a < b : a가 b보다 작으면 True, 크면 False -> True
a >= b : a가 b보다 크거나 같으면 True, 작으면 False -> False
a <= b : a가 b보다 작거나 같으면 True, 크면 False -> True
'''

print("산술 연산자")

print(a // b)
print(a % b)
print(a ** b)

s1, s2 ,s3 ="100", "100.123", "99999999999999999"
print(int(s1)+1, float(s2)+1, int(s3)+1)
a = 100; b = 100.123
print(str(a) + '1', str(b) + '1')

## 변수 선언 부분 ##
money, c500, c100, c50, c10 = 0, 0, 0, 0, 0

## 메인 코드 부분 ##
money = int(input("\n 교환할 돈은 얼마입니까?: ")) ##동전으로 교환할 돈(money)과 500원, 100원, 50원, 10원짜리 동전의 개수를 저장할 변수 초기화##

c500 = money // 500     ##500원짜리 동전의 개수##
money %= 500            ##다시 money를 500으로 나눈 후 나머지 값 지정##

c100 = money // 100    ##100원짜리 동전의 개수##
money %= 100           ##다시 money를 100으로 나눈 후 나머지 값 지정##

c50 = money // 50      ##50원짜리 동전의 개수##
money %= 50            ##다시 money를 50으로 나눈 후 나머지 값 지정##

c10 = money // 10      ##10원짜리 동전의 개수##
money %= 10            ##다시 money를 10으로 나눈 후 나머지 값 지정##

print("\n500원짜리 ==> %d개" % c500)
print("100원짜리 ==> %d개" % c100)
print("50원짜리 ==> %d개" % c50)
print("10원짜리 ==> %d개" % c10)
print("바꾸지 못한 잔돈 ==> %d원" % money)

## 지폐 변수 선언 부분 ##
b50000, b10000, b5000, b1000 = 0, 0, 0, 0

## 지폐 계산 부분 ##
money = int(input("\n 지폐로 교환할 돈은 얼마입니까?: "))

b50000 = money // 50000
money %= 50000

b10000 = money // 10000
money %= 10000

b5000 = money // 5000
money %= 5000

b1000 = money // 1000
money %= 1000

print("\n50000원짜리 ==> %d장" % b50000)
print("10000원짜리 ==> %d장" % b10000)
print("5000원짜리 ==> %d장" % b5000)
print("1000원짜리 ==> %d장" % b1000)
print("바꾸지 못한 잔돈 ==> %d원" % money)



print("\n 대입 연산자")
a = 9
a += 3
print(a)

a = 9
a -= 3
print(a)
a *= 3
print(a)
a /= 3
print(a)
a //= 3
print(a)
a %= 3
print(a)
a **= 3
print(a)


print("\n관계 연산자")
a = 3
b = 9
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

'''
print("논리 연산자")
a = 9
b = 2
##and : a와 b가 모두 True이면 True, 하나라도 False이면 False##
print(a > 100) and (b > 10)
print(a > 100) or (b > 10)
print(not (a > 100))
'''

a = 99
if a < 100 :
    print("100보다 작군요.")
    print("거짓이므로 이 문장은 안보이겠죠?")

print("\n프로그램 끝")

a = int(input("\n정수를 입력하세요: "))

if a % 2 == 0 :
    print("입력한 정수는 짝수입니다.\n")
else :
    print("입력한 정수는 홀수입니다.\n")

a = 75
if a > 50 :
    if a < 100 :
        print("50보다 크고 100보다 작군요.")
    else :
        print("와~ 100보다 크군요.")
else :
    print("에고~ 50보다 작군요.")

score = int(input("\n점수를 입력하세요: "))

if score >= 90 :
    print("A")
else :
    if score >= 80 :
        print("B")
    else :
        if score >= 70 :
            print("C")
        else :
            if score >= 60 :
                print("D")
            else :
                print("F")
print("\n학점입니다. ^^")

