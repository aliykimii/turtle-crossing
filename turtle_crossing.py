import random
from turtle import Turtle
from turtle import Screen
import time

screen = Screen()
screen.setup(width=700, height=600)
screen.tracer(0)

#Level display
fonts = "Courier", 24, "normal"
level = 1
display = Turtle()
display.hideturtle()
display.penup()
display.goto(-300,250)
display.write(f"Level : {level}", "left", font = fonts)

def game_over():
      fonts = "Corbel Bold", 24, "normal"
      over = Turtle()
      over.hideturtle()
      over.penup
      over.goto(-75,0)
      over.write("Game Over", "middle",font = fonts)

colors = ["purple","blue","black","red","cyan"]
cars = []

#Creating Cars
def create_cars():
      random_chance = random.randint(1,6)
      if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.speed(0)
            random_y = random.randint(-250,250)
            new_car.goto(400,random_y)
            new_car.shapesize(stretch_wid = random.randint(1,2),stretch_len = random.randint(2,3)) 
            new_car.color(random.choice(colors))    
            cars.append(new_car)
#Making The Cars Move            
car_speed = 5
def moving_cars():
      create_cars()
      for i in cars:
            i.speed(5)
            i.backward(car_speed)
#User
starting_point = (0,-280)
finish_point_y = 280
      
user = Turtle("turtle")
user.penup()
user.goto(starting_point)
user.setheading(90)
     
def up():
      user.forward(10)

screen.onkey(up,"Up")
screen.listen()
      
game_on = True                       
while game_on == True:
      time.sleep(0.1)
      screen.update()
      moving_cars()
      for i in cars:
            if i.distance(user) < 20: 
                  game_on =False
                  display.clear()
                  game_over()
      if user.ycor() > finish_point_y:
            user.goto(starting_point)
            car_speed += 2
            display.clear()
            level += 1
            display = Turtle()
            display.hideturtle()
            display.penup()
            display.goto(-300,250)
            display.write(f"Level : {level}", "left", font = fonts)
  
      
     




      
