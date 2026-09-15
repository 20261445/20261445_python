'''
a =int(input("첫번째 값: "))
b =int(input("두번째 값: "))

result1 = a + b
result2 = a - b
result3 = a * b
result4 = a / b

print(result1)
print(result2)
print(result3)
print(result4)

data = '안녕' +\
       '하세요? ' +\
       '파이썬!'
print(data)

data = '안녕\n파이썬 \n화요일 수업이지'
print(data)
'''

import turtle
import random

## 함수 선언 부분 ##
def screenLeftClick(x, y) :
    global r, g, b
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x,y)

def screenRightClick(x, y) :
    turtle.penup()
    turtle.goto(x, y)

def screenMidClick(x, y) :
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()

## 변수 선언 부분 ##
pSize = 10
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()