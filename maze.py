# Simple maze game 

# Screen Area 600 x 600 
# Sprites 24 x 24 
# Grid 25 x 25 
# Advantage - 0,0 is the center of a sprite as there is an odd number of blocks; Fewer blocks to worry about 
# Disadvantage - harder to calculate the sprite centers
# Coordinates: 
# Top Left Block -288,288
# Top Right Block 288,288
# Bottom Left Block -288,-288
# Bottom Right Block 288, -288

import turtle # Importing turtle tool into python
import math

wn = turtle.Screen() #Creating Screen //turtle module * Screen method
wn.bgcolor("black") # background color, black
wn.title("A maze Game By: iNode.code ~A-maze-ing~") # Title for game
wn.setup(700,700) #Width & Height

# Create Pen
class Pen(turtle.Turtle): # Creating class "pen"[Class defines object] Pen is child of turtle module & Turtle class [Pen is turtle]
    def __init__(self):   # Function "__init__[initialize]" // self refers to object
        turtle.Turtle.__init__(self) # Initializing class
        self.shape("square") # Define shape
        self.color("white") # white color
        self.penup() # Pen up because we dont want to draw
        self.speed(0) # Animation speed set to zero so it can be played like a game[Is the fastest setting]
        
# Create Player
class Player(turtle.Turtle): 
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        # Calculate the spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        # Calculate the spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        # Calculate the spot to move to
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor() 

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)


    def go_right(self):
        # Calculate the spot to move to
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor() 

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2) )

        if distance < 5:
            return True
        else:
            return False


# Create Treasure
class Treasure(turtle.Turtle): 
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self): # Cant actually destroy turtle, moving it off screen and hiding it.
        self.goto(2000, 2000)
        self.hideturtle()

# Create level list
levels = [""] # Levels starting at 0

# Define first level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX", # Down is y coordinate // x is across coordinate
"XXXXXX               XXXX", 
"XXXXXX   XXXXXXXX     XXX",
"XXT XX   XXXXXXXX  P  XXX",
"XX  XX   XXXXXXXXXXXXXXXX",
"XX  XX               XXXX",
"XX   XX  XXXXX  XXX  XXXX",
"XX   XXXXXXXXX  XXX  XXXX",
"XX              XXX    XX",
"XXXXXX  XXXXXX  XXXXXXXXX",
"XXXXXX  XXXXXX  XXXXXXXXX",
"XXXXXX  XXXXXX         XX",
"X       XXXXXXXXX  XXXXXX",
"X XXXXXXXXXXXXXXX  XXXXXX",
"X X                  XXXX",
"X X  XXXXXXXXXXXXXX  XXXX",
"X X            XXXX TXXXX",
"X X  XXXXXXXX  XXXXXXXXXX",
"X X  XXXXXXXX    XXXXXXXX",
"X X      XXXXXXXXXXXXXXXX",
"X XXXXX             XXXXX",
"X XXXXXXXXXXXXXX  XXXXXXX",
"XTXXXXX    X           XX",
"XXT             XXXX   XX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]

# Add a treasures list
treasures = []

# Add maze to mazes list
levels.append(level_1)

# Create Level Setup Function
def setup_maze(level):
    for y in range(len(level)): # number of rows down
        for x in range(len(level[y])): # checks the lengths of characters across
            # Get the character at each x,y coordinate
            # note the order of y and x in the next line
            character = level[y][x]
            # Calculate the screen x,y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            #Check if it is an X (representing a wall)
            if character == "X":
                pen.goto(screen_x, screen_y) # If there IS an X, move the pen to the X and Y Coord.
                pen.stamp() # Puts on screen, and leaves it there
                # Add coordinates to wall list
                walls.append((screen_x, screen_y))
            
            #Check if it is a P (representing the player)
            if character == "P":
                player.goto(screen_x, screen_y)

            #Chyeck if it is a T (representing the treasure)
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))

# Create class instances
pen = Pen()
player = Player()

# Create wall coordinate list
walls = [] 

# Set up the level
setup_maze(levels[1]) # Calling Function
print (walls)

# Keyboard Binding
wn.onkey(player.go_left,"a")
wn.onkey(player.go_right,"d")
wn.onkey(player.go_up,"w")
wn.onkey(player.go_down,"s")
wn.listen()


#Turn off screen updates
wn.tracer(0)

#Main Game Loop
while True:
    # Check for player collision with treasure
    # Iterate through treasure list
    for treasure in treasures:
        if player.is_collision(treasure):
            # Add the treasure gold to the player gold
            player.gold += treasure.gold
            print ("Player Gold: {}".format(player.gold))
            # Destory the treasure
            treasure.destroy()
            # Remove the treasure from the treasures list
            treasures.remove(treasure)


    # Update screen
    wn.update()

wn.mainloop()