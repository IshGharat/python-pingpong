
import turtle

window=turtle.Screen()
window.title("CodeRunner Ping Pong")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)

#Score
score1=0
score2=0

#Player 1
Player1=turtle.Turtle()
Player1.speed(0)
Player1.shape("square")
Player1.color("#e07762")
Player1.penup()
Player1.goto(-350,0)
Player1.shapesize(stretch_wid=5,stretch_len=.5)


#Player 2
Player2=turtle.Turtle()
Player2.speed(0)
Player2.shape("square")
Player2.color("#3aeac4")
Player2.penup()
Player2.goto(350,0)
Player2.shapesize(stretch_wid=5,stretch_len=.5)


#Ball
Ball=turtle.Turtle()
Ball.speed(0)
Ball.shape("square")
Ball.color("#0BDFFF")
Ball.penup()
Ball.dx=0.07
Ball.dy=0.07

#Pen
Pen=turtle.Turtle()
Pen.speed(0)
Pen.color("#0BDFFF")
Pen.penup()
Pen.hideturtle()
Pen.write("\t\tPlayer 1\tPlayer 2\n\nUp\t\tw\t\tUp Arrow\n\nDown\t\ts\t\tDown Arrow",align="center",font=("Courier",12,"normal"))
turtle.delay(3000)
Pen.clear
Pen.goto(0,260)
Pen.write("Player 1: 0, Player 2: 0",align="center",font=("Courier",24,"normal"))


#Moving the paddles

def Paddle1_Up():
    y=Player1.ycor()
    y+=20
    if(y<=240):
        Player1.sety(y)

def Paddle1_Down():
    y=Player1.ycor()
    y-=20
    if(y>=-240):
        Player1.sety(y)

def Paddle2_Up():
    y=Player2.ycor()
    y+=20
    if(y<=240):
        Player2.sety(y)

def Paddle2_Down():
    y=Player2.ycor()
    y-=20
    if(y>=-240):
        Player2.sety(y) 

def Set_Start():
    return True

#Keyboard binding
window.listen()
window.onkeypress(Paddle1_Up,"w")
window.onkeypress(Paddle1_Down,"s")

window.onkeypress(Paddle2_Up,"Up")
window.onkeypress(Paddle2_Down,"Down")


while True:
    window.update()
    newx=Ball.xcor()+Ball.dx
    newy=Ball.ycor()+Ball.dy
    Ball.setx(newx)
    Ball.sety(newy)

    #Border checking
    if Ball.ycor()>290:
        Ball.sety(290)
        Ball.dy*=-1
    elif Ball.ycor()<-290:
        Ball.sety(-290)
        Ball.dy*=-1

    if Ball.xcor()>390:
        score1+=1
        Pen.clear()
        Pen.write("Player 1: {}, Player 2: {}".format(score1,score2),align="center",font=("Courier",24,"normal"))
        Ball.goto(0,0)
        Ball.dx*=-1
        Ball.dy*=-1
    elif Ball.xcor()<-390:
        score2+=1
        Pen.clear()
        Pen.write("Player 1: {}, Player 2: {}".format(score1,score2),align="center",font=("Courier",24,"normal"))
        Ball.goto(0,0)
        Ball.dx*=-1

    if (-350<Ball.xcor()<-340) and (Ball.ycor()<Player1.ycor()+50) and (Ball.ycor()>Player1.ycor()-50):
        Ball.dx*=-1
    if (340<Ball.xcor()<350) and (Ball.ycor()<Player2.ycor()+50) and (Ball.ycor()>Player2.ycor()-50):
        Ball.dx*=-1

    
