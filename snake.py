import turtle
import time
import random

posp = 0.1


#Scores
score = 0
high_score = 0

#Screen
wn = turtle.Screen()
wn.title('Juego de Snake')
wn.bgcolor('black')
wn.setup(width = 600, height = 600)
wn.tracer(0)

#Food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.penup()
food.goto(0,100)
food.color('red')

#Snake Body
body = []

#Scores Text
text = turtle.Turtle()
text.speed(0)
text.color('white')
text.penup()
text.hideturtle()
text.goto(0,260)
text.write('Score: {}    High Score: {}'.format(score, high_score), align='center', font=('Courier', 24, 'normal'))

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.penup()
head.goto(0,0)
head.direction = 'stop'
head.color('green')

#Mov Functions
def up():
    head.direction = 'up'

def down():
    head.direction = 'down'

def left():
    head.direction = 'left'

def right():
    head.direction = 'right'

def mov():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)
    elif head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)

#Listen Keyboard
wn.listen()
wn.onkeypress(up, 'Up')
wn.onkeypress(down, 'Down')
wn.onkeypress(right, 'Right')
wn.onkeypress(left, 'Left')

#Loop
while True:
    wn.update()

    #Food Colision
    if head.distance(food) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x,y)

        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape('square')
        new_body.penup()
        new_body.color('darkgreen')
        body.append(new_body)

        score += 10

        if score > high_score:
            high_score = score

        text.clear()
        text.write('Score: {}    High Score: {}'.format(score, high_score), align='center', font=('Courier', 24, 'normal'))


    totalBodys = len(body)

    #Follow Body
    for index in range(totalBodys -1, 0, -1):
        x = body[index - 1].xcor()
        y = body[index - 1].ycor()
        body[index].goto(x,y)
    
    if totalBodys > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x,y)

    #Screen Colision
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        for i in body:
            i.hideturtle()
        body.remove(new_body)
        body.clear()
        head.direction = 'stop'
        head.goto(0,0)
        score = 0
        text.clear()
        text.write('Score: {}    High Score: {}'.format(score, high_score), align='center', font=('Courier', 24, 'normal'))

    mov()

    #Body Colision
    for i in body:
        if i.distance(head) < 20:
            for i in body:
                i.hideturtle()
            body.remove(new_body)
            body.clear()
            head.direction = 'stop'
            head.goto(0,0)
            score = 0
            text.clear()
            text.write('Score: {}    High Score: {}'.format(score, high_score), align='center', font=('Courier', 24, 'normal'))

    time.sleep(posp)