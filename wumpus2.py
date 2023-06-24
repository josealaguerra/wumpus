
import turtle
import time


sizeSquare=40
waitTime = 0.1
screenWidth=600
screenHeight=600

wn = turtle.Screen()
wn.title("Wumpus")
wn.bgcolor("yellow")
wn.setup(width=screenWidth, height=screenHeight)
wn.tracer(0)






trtl = turtle.Turtle()
trtl.goto(-screenWidth/2,screenHeight/2)


# method to draw square
def draw():
   
  for i in range(4):
    trtl.forward(sizeSquare)
    trtl.left(90)
   
  trtl.forward(sizeSquare)
   
  
     
# Driver Code
if __name__ == "__main__" :
      
    # set wnreen
    # wn.setup(screenWidth, screenHeight)
       
    # set turtle object speed
    trtl.speed(100)
       
    # loops for board
    for i in range(8):
       
      # not ready to draw
      trtl.up()
       
      # set position for every row
      trtl.setpos(0, sizeSquare * i)
       
      # ready to draw
      trtl.down()
       
      # row
      for j in range(8):
       
        # conditions for alternative color
        if (i + j)% 2 == 0:
          col ='black'
       
        else:
          col ='white'
       
        # fill with given color
        trtl.fillcolor(col)
       
        # start filling with colour
        trtl.begin_fill()
       
        # call method
        draw()
        # stop filling
        trtl.end_fill()
       
    # hide the turtle
    # trtl.hideturtle()

trtl.speed(0)
trtl.shape("square")
trtl.color("red")
trtl.penup()
trtl.goto(0,0)
trtl.direction="stop"






def arriba():
    trtl.direction = "up"

def abajo():
    trtl.direction = "down"

def izquierda():
    trtl.direction = "left"

def derecha():
    trtl.direction = "right"            





def mov():
    if trtl.direction == "up":
        y = trtl.ycor()
        trtl.sety(y + 20)

    if trtl.direction =="down":
        y = trtl.ycor()
        trtl.sety(y - 20 )

    if trtl.direction =="left":
        x = trtl.xcor()
        trtl.setx(x - 20 ) 

    if trtl.direction =="right":
        x = trtl.xcor()
        trtl.setx(x + 20 )






wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")


while True:
    wn.update()
    mov()

    time.sleep(waitTime)

