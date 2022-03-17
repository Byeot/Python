import turtle as t

t.shape("turtle")
t.speed(0)
t.pensize(20)

# 블랙 원 그리기
t.circle(100)

t.up()
t.forward(240)
t.down()
t.pencolor('red') #2번위치의 원
t.circle(100)

t.up()
t.backward(480)
t.down()
t.pencolor('blue') #1번 위치의 원
t.circle(100)

t.up()
t.right(90)
t.forward(120)
t.left(90)
t.forward(120)
t.down()
t.pencolor('yellow') #4번 위치의 원
t.circle(100)

t.up()
t.forward(240)
t.down()
t.pencolor('green') #5번 위치의 원
t.circle(100)


t.done()