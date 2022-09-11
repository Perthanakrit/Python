import turtle
def movement1(m_left,m_forward):
    t.penup()# no drawing when moving.
    t.left(m_left)
    t.forward(m_forward)

def movement2(m_right,m_forward):
    t.penup()
    t.right(m_right)
    t.forward(m_forward)
def movement(m_right, m_forward, m_left,m_backward):
    t.penup()
    t.right(m_right)
    t.forward(m_forward)
    t.left(m_left)
    t.backward(m_backward)

t = turtle.Turtle()
t.speed(8)
#E
t.right(0)
t.pendown()
t.left(70)
t.forward(310)
t.right(140)
t.forward(310)

t.penup()
t.right(180)
t.forward(140)
t.left(70)
t.pendown()

t.forward(125)
movement(180,200,0,0)
movement(0,0,90,130)
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
t.forward(200)
turtle.done()