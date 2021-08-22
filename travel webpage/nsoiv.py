import turtle

col = ('red','yellow','cyan','green','blue','white')

t=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('black')
t.speed(30)


for i in range(500):
    
    t.color(col[i%6])
    t.forward(i*4) 
    t.backward(i*2)
    t.left(300)
    t.width(1)    
turtle.done() 


