import turtle

def movement1(m_left,m_forward):
    t.penup()# no drawing when moving.
    t.left(m_left)
    t.forward(m_forward)
    t.pendown()

def movement2(m_right,m_forward):
    t.penup()
    t.right(m_right)
    t.forward(m_forward)
    t.pendown()

def movement(m_right, m_forward, m_left,m_backward):
    t.penup()
    t.right(m_right)
    t.forward(m_forward)
    t.left(m_left)
    t.backward(m_backward)


t = turtle.Turtle()
s= turtle.Screen()
s.bgcolor("black")
t.speed(25)
t.pensize(7)
t.pencolor("yellow")

t.penup()
t.backward(450)
t.left(90)
t.forward(150)
t.pendown()
#H
t.forward(200)
t.penup()
t.backward(100)
t.pendown()

t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
t.backward(200)

t.penup()
t.right(90)
t.forward(40)
t.pendown()

t.left(70)
t.forward(210)
t.right(140)
t.forward(210)

t.penup()
t.right(180)
t.forward(105)
t.left(70)
t.pendown()

t.forward(67)

movement(0,0,0,150)
movement(90,0,0,100)
t.pendown()
t.forward(200)
t.right(90)
t.pendown()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

movement(180,150,0,0)
movement(0,0,90,100)
t.pendown()
t.forward(200)
t.right(90)
t.pendown()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

movement(180,150,90,0)
movement(0,100,180,0)
t.pendown()
t.pencolor("#00EEEE")
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

movement(180,100,0,0)
movement(90,50,90,0)
t.pendown()

t.forward(120)
t.right(90)
t.forward(550)
t.left(90)
t.forward(200)

movement(180,180,0,0)
t.right(150)
t.pendown()

t.forward(212)
t.left(150)
t.forward(180)

movement(90,160,0,0)
movement(90,180,0,0)
t.right(90)
t.pendown()
#E
t.forward(130)
t.right(90)
t.forward(180)
t.right(90)
t.forward(130)

movement(180,130,90,0)
t.forward(90)
t.pendown()

t.left(90)
t.forward(130)

movement(0,50,270,90)
t.pendown()

t.forward(150)
for i in range(180):
    t.left(1)
    t.forward(0.7)
t.forward(150)
movement(180,150,0,0)
t.pendown()

for i in range(180):
    t.left(1)
    t.forward(0.7)
t.forward(150)

movement(90,0,0,600)
movement(0,0,90,200)
t.right(180)
t.pendown()
t.pencolor("lime")
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)

movement(180,150,0,0)
movement(90,50,90,0)
t.pendown()

t.forward(150)

#E
movement(180,10,0,0)
movement(90,200,0,0)
t.right(180)
t.pendown()
t.forward(120)
t.right(90)
t.forward(290)
t.right(90)
t.forward(120)

movement(180,120,90,0)
t.forward(140)
t.pendown()

t.left(90)
t.forward(120)
#A
movement(0,30,90,150)
t.right(90)
t.pendown()
t.left(70)
t.forward(310)
t.right(140)
t.forward(310)

t.penup()
t.right(180)
t.forward(145)
t.left(70)
t.pendown()

t.forward(124)
#R
movement(180,200,0,0)
movement(0,0,90,140)
t.pendown()
t.forward(290)
t.right(90)
t.pendown()
t.forward(150)
t.right(90)
t.forward(150)
t.right(90)
t.forward(150)
movement(180,50,0,0)
t.pendown()
t.right(55)
t.forward(170)

turtle.done()