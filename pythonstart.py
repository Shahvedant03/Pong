import turtle
from turtle import Turtle

win = turtle.Screen()
win.title("Pong by @Flamekaiser29")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Scoring system
score_a = 0
score_b = 0



# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball: Turtle = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# scores-pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("PlayerA: {} PlayerB: {}".format(score_a,score_b), align="center", font=("Courier",12,"normal"))



# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)



# keyboard binding
win.listen()
win.onkeypress(paddle_a_up,"w")
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_b_up,"8")
win.onkeypress(paddle_b_down,"2")




# main game loop
while True:
    win.update()

# ball movement
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor()> 290 :
       ball.sety(290)
       ball.dy *= -1

    if ball.ycor() < -290:
       ball.sety(-290)
       ball.dy *= -1

    if ball.xcor()> 390 :
       ball.goto(0,0)
       ball.dx *= -1
       score_a += 1
       pen.clear()
       pen.write("PlayerA: {} PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 12, "normal"))

    if ball.xcor()< -390 :
       ball.goto(0, 0)
       ball.dx *= -1
       score_b += 1
       pen.clear()
       pen.write("PlayerA: {} PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 12, "normal"))

       # collision
    if (ball.xcor()> 340 and ball.xcor()< 350)and(ball.ycor()<paddle_b.ycor()+40 and ball.ycor()> paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1


    if (ball.xcor()<- 340 and ball.xcor()> -350)and(ball.ycor()<paddle_a.ycor()+40 and ball.ycor()> paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1