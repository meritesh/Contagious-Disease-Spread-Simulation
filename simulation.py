import turtle
import random
import math

wn = turtle.Screen()
wn.title("Simulation")
wn.bgcolor("black")
wn.setup(width=1500, height=720)
wn.tracer(0)

#setting paramaters
number_of_people=1000
back_to_healthy=True
healthy_after_time = 500
min_distance_to_get_infected = 10
speed_of_simulation = 1

#initialization
balls = []
for i in range(number_of_people):
    balls.append(turtle.Turtle())
for ball in balls:
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.speed(0)
    x = random.randint(-750,750)
    y = random.randint(-380,380)
    ball.setposition(x,y)
    ball.shapesize(0.1)
    ball.dx = random.uniform(-1,1)*speed_of_simulation
    ball.dy = random.uniform(-1,1)*speed_of_simulation
    ball.status = 0
    ball.timer = 0


#patient 0
balls[0].color("red")
balls[0].status = 1
balls[0].timer = healthy_after_time

#main loop
while True:
    wn.update()

    for ball in balls:    

        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() > 380:
            ball.sety(380)
            ball.dy *= -1

        if ball.xcor() > 750:
            ball.setx(750)
            ball.dx *= -1
        
        if ball.ycor() < -380:
            ball.sety(-380)
            ball.dy *= -1

        if ball.xcor() < -750:
            ball.setx(-750)
            ball.dx *= -1
    
    for i in range(number_of_people):
        for j in range(i+1,number_of_people):
            if (abs(balls[i].xcor()-balls[j].xcor())<min_distance_to_get_infected) and (abs(balls[i].ycor()-balls[j].ycor())<min_distance_to_get_infected):
                if(balls[i].status==1 or balls[j].status==1):
                    #print(i,j)
                    balls[i].status=1
                    balls[j].status=1
                    balls[i].color("red")
                    balls[j].color("red")
                    if(back_to_healthy):
                        balls[i].timer = healthy_after_time
                        balls[j].timer = healthy_after_time
    if(back_to_healthy):
        for ball in balls:
            if(ball.timer>0):
                #print(ball.timer)
                ball.timer = ball.timer - 1
            if(ball.timer==0):
                ball.color("white")
                ball.status=0