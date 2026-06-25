#DEFINING and caling  python functions 

def my_function() :
    print("HI this is my first function")


my_function()    

## try those bellow commands on https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
#turn_left()  turning to left
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

turn_around()
turn_right()


turn_left()    
move()
move()
turn_right()
move()
move()
turn_right()
move()
move()
turn_right()
move()
move()
turn_around()


####https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
###try bellow commands on this web page

def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    
    
for i in range(6):
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()