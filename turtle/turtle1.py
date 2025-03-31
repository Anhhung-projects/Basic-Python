import turtle as t

#setup
t.setup()
t.title('Mouse Click')
t.showturtle() #Hiện rùa, hideturtle() để ẩn rùa
t.shape('turtle')
t.penup()
t.seth(0)

def printxy(x,y):
    t.goto(x,y)
    print("Co-ordinates:",x,y)
    
t.onscreenclick(printxy)
t.mainloop()
