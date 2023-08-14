from turtle import *
from random import randint


s_width = 200
s_height = 180

class Sprite(Turtle):
    def __init__(self, x, y, shp, clr):
        Turtle.__init__(self)
        self.penup()
        self.goto(x, y)
        self.color(clr)
        self.shape(shp)
        self.left(180)
        self.step = 10
        self.points = 0


    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)
    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())
    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())

    def is_collide(self, sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        if dist < 20:
            return True
        return False





class Enemy(Sprite):
    def __init__(self, x, y, shp, clr):
        Sprite.__init__(self, x, y, shp, clr)
        self.goto(x, y)
        self.color(clr)
        self.shape(shp)
        self.speed(10)
        self.step = 10

    def move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(self.x_start, self.y_start)
        self.setheading(self.towards(self.x_end, self.y_end))

    def make_step(self):
        self.fd(self.step)
        if self.distance(self.x_end, self.y_end) < self.step:
            self.move(self.x_end, self.y_end, self.x_start, self.y_start)



player = Sprite(170, 160, 'turtle', 'green')
coin = Sprite(-170, -150, 'circle', 'yellow')

enemy1 = Enemy(s_width, -90, 'triangle', 'red')
enemy1.move(s_width, -90, -s_width, -90)
enemy2 = Enemy(-s_width, 90, 'triangle', 'red')
enemy2.move(-s_width, 90, s_width, 90)
enemy3 = Enemy(-90, s_height, 'triangle', 'red')
enemy3.move(-90, s_height, -90, -s_height)

scr = player.getscreen()
scr.listen()
scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_down, 'Down')
scr.onkey(player.move_left, 'Left')
scr.onkey(player.move_right, 'Right')
score = 0
while score < 3:
    enemy1.make_step()
    enemy2.make_step()
    enemy3.make_step()
    if player.is_collide(coin):
        score += 1
        coin.goto(randint(-80, 80), randint(-80, 80))

    if player.is_collide(enemy1) or player.is_collide(enemy2) or player.is_collide(enemy3):
        coin.hideturtle()
        break
if score == 3:
    enemy1.hideturtle()
    enemy2.hideturtle()
    enemy3.hideturtle()
