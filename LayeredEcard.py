import turtle
import math

'''
This program draws 3D-like models for an ecard.
File name: Layered_Ecard.py
Author: Joseph Thurlow
'''
# initialize turtle & window
t = turtle.Turtle()
wn = turtle.Screen()
wn.setworldcoordinates(0, 0, 1000, 1000)
t.ht()
wn.bgcolor("lightgreen")
t.speed(0)

def colorSelect(r, g, b, colorCount):
    '''
    Converts the original RGB color into 2 different darker colours for shading
    the cube then converts the RGB value into HEX.

    Parameters:
    colorCount (int): Tells colorSelect what side of the block is being drawn next
    r, g, b (int): The color values from 0-255 taken from the model data file

    Returns:
    hexValue (str): The hex color value used to color the parallelogram
    '''
    if colorCount == 0:
        r = int(r/1.5)
        g = int(g/1.5)
        b = int(b/1.5)
        hexValue = '#%02x%02x%02x' % (r, g, b)
    elif colorCount == 1:
        r = int(r/1.8)
        g = int(g/1.8)
        b = int(b/1.8)
        hexValue = '#%02x%02x%02x' % (r, g, b)
    else:
        hexValue = '#%02x%02x%02x' % (r, g, b)
    return hexValue

def block(t, color, size):
    '''
    This function creates the blocks that are used to create the environment and object
    Parameters:
    angles (list): Lists the angles the turtle needs to turn to create a parallelogram
    colorCount (int): Iterates by 1 each time one side of a block is completed
    count (int): Counts how many times the turtle has turned. Gets reset to 0 after each parallelogram
    '''
    # Set variables
    angles = [120, 60, 120, 60]
    colorCount = 0
    for i in range(3): # This for loop changes the color for each face
        colors = colorSelect(color[0], color[1], color[2], colorCount)
        colorCount = colorCount + 1
        t.fillcolor(colors)
        t.begin_fill()
        count = 0
        for angle in angles: # This for loop creates each face of the cube
            t.forward(size)
            if count < 3:
                t.left(angle)
                count = count + 1
            else:
                t.right(angle)
        t.end_fill()

def environment(t, color, size, model):
    '''
    Creates the first layer/environment and records the coordinates of each block on the environment plane
    Parameters:
    l (list): The list where the coordinates are stored
    x, y (int): Takes the x & y values from the data model list
    xLen, yLen (int): Changes the size of the environment according to values in the model data list
    xStart, yStart (int): Used to calculate the position of the next row

    Returns:
    l (list): The locations of all the blocks that make up the environment are returned
    '''

    l = []
    x = model[0][0]
    y = model[0][1]
    t.up()
    t.setpos(x, y)
    t.setheading(270)
    t.down()
    xLen = model[1][0]
    yLen = model[1][1]
    # Create the environment/plane
    for yMove in range(yLen):
        xStart = x + ((size *(math.sin(math.radians(60))))*yMove)
        yStart = y - ((size *(math.cos(math.radians(60))))*yMove)
        t.up()
        t.goto(xStart, yStart)
        t.down()
        for xMove in range(xLen):
            block(t, color, blockSize)
            # Record the points for the next layer
            l.append(t.pos())
            t.up()
            t.right(60)
            t.forward(size)
            t.left(60)
            t.down()
    # Coordinates are returned
    return l

def blockObject(t, size, layers):
    '''
    This function creates the model using the model data or layers
    Parameters:
    points (list): Calls the environment function and stores the coordinates for each environment block
    height (int): Is the number of items in the model data list
    '''
    # NOTE:layers[0] is a parameter that holds the environment data for the model
    t.pencolor("black")
    points = environment(t, layers[0][2], blockSize, layers[0])
    height = len(layers)
    for num in range(1, height):
        for layer in layers[num]:
            if type(layer) == list:
                # Checks if the data is a color value (or list)
                # Sets the new color value to the selected color
                color = layer

            else:
                # Moves the turtle to the correct position to draw (according to the model data)
                # Creates a block at that location.
                t.up()
                t.goto(points[layer][0], points[layer][1] + (size*(num)))
                t.down()
                block(t, color, size)

# Main settings
blockSize = 20 # change this value to change the size of the blocks
t.pensize(blockSize/10) # Pensize scales with the size of the blocks

# Defining model colors
# Ryu
skin = [240, 165, 105]
red = [230, 25, 25]
black = [50, 50, 50]
white = [225, 225, 225]
hair = [100, 70, 25]
darkSkin = [215, 140, 75]
# Bulbasaur
greenSkin = [10, 228, 142]
blueSkin = [10, 201, 149]
lgreenSkin = [150, 230, 30]
red = [215, 17, 27]
# Mario
marioBrown = [110, 90, 5]
marioRed = [255, 50, 50]
marioSkin = [250, 190, 130]
marioGold = [240, 164, 0]

# Model data files
Ryu = [
          [[500, 200], [5, 5], [200, 200, 200]],
          [skin, 7, 17],
          [white, 7, 17],
          [17],
          [black, 8, 16, 13, 17, 18, red, 22],
          [white, 8, 16, 13, 17, 18, skin, 21],
          [white, 8, 16, 13, 17, 18, skin, 21],
          [white, 8, 16, skin, 13, white, 17, 18, skin, 22],
          [red, 20],
          [red, 15, hair, 16, skin, 8, 13, 17, 18],
          [red, 10, hair, 16, darkSkin, 8, 13, 17, 18],
          [red, 10, 8, 16, 13, 17, 18, hair, 9],
          [hair, 6, 11, 16, 7, 8, 12, 13, 17, 18, 9, 14]]
Bulbasaur = [
    [[700, 700], [10, 11], [130, 80, 50]],
    [greenSkin, 8, 18, 27, 28, 58, 68, 70, 71, 77, 78],
    [greenSkin, 8, 17, 18, blueSkin, 58, 67, 68],
    [blueSkin, 8, greenSkin, 18, 27, 37, 47, 58, 67, 68, 76, 86, 93, 94, 95],
    [greenSkin, 17, blueSkin, 27, 37, greenSkin, 47, 57, 87, 96, 103, 104, 105],
    [lgreenSkin, 17, 27, greenSkin, 47, 68, 78, 87, red, 96, greenSkin, 103, 104, 105],
    [lgreenSkin, 5, 6, 17, 27, 37, 46, greenSkin, 68, 78, 87, white, 96, blueSkin, 103, greenSkin, 104, 105],
    [lgreenSkin, 16, 27, 37, 46, greenSkin, 68, 78, 87, 96, 103, 104, blueSkin, 105],
    [lgreenSkin, 4, 5, 15, 16, 26, 33, 35, 36, 45, greenSkin, 67, 76, 77, 86, blueSkin, 93, 94, greenSkin, 95],
    [lgreenSkin, 14, 23, 24, 25, 34, greenSkin, 62, 63, 64, 65, 66, 67, 73, 74, 75, 83, 84, 85],
    [greenSkin, 63, 65, 66]
]
Mario = [
    [[200, 600], [3, 12], [0, 230, 30]],
    [marioBrown, 1, 4, 7, 10, 25, 28, 31, 34],
    [4, 7, 10, 25, 28, 31],
    [marioRed, 7, 10, 13, 22, 25, 28],
    [marioSkin, 1, 4, marioRed, 7, 10, 13, 16, 19, 22, 25, 28, marioSkin, 31, 34],
    [marioSkin, 1, 4, 7, marioRed, 10, 13, 16, 19, 22, 25, marioSkin, 28, 31, 34],
    [marioSkin, 1, 4, marioBrown, 7, marioRed, 10, marioGold, 13, marioRed, 16, 19, marioGold, 22, marioRed, 25, marioBrown, 28, marioSkin, 31, 34],
    [marioBrown, 1, 4, 7, 10, marioRed, 13, 16, 19, 22, marioBrown, 25, 28, 31, 34],
    [marioBrown, 4, 7, 10, marioRed, 13, marioBrown, 16, 19, marioRed, 22, marioBrown, 25, 28, 31],
    [marioBrown, 7, 10, marioRed, 13, marioBrown, 16, 19, 22],
    [marioSkin, 10, 13, 16, 19, 22, 25, 28],
    [marioBrown, 4, 7, marioSkin, 10, 13, 16, 19, marioBrown, 22, 25, 28, 31],
    [marioBrown, 4, marioSkin, 7, marioBrown, 10, 13, marioSkin, 16, 19, 22, marioBrown, 25, marioSkin, 28, 31, 34],
    [marioBrown, 4, marioSkin, 7, marioBrown, 10, marioSkin, 13, 16, 19, marioBrown, 22, marioSkin, 25, 28, 31],
    [marioBrown, 7, 10, 13, marioSkin, 16, 19, marioBrown, 22, marioSkin, 25],
    [marioRed, 7, 10, 13, 16, 19, 22, 25, 28, 31],
    [marioRed, 10, 13, 16, 19, 22],
]
models = [Ryu, Mario, Bulbasaur]

'''
Calls the blockObject function to draw the environment and model
Parameters of blockObject: (turtle, block size, model data file)
The model data file contains:
 -the start location of the environment 
 -the size of the environment
 -the color of the environment
 -the data(color and location) that produces the model
NOTE: It will take a while to draw some/all of the models...
'''
for model in models:
    blockObject(t, blockSize, model)

wn.exitonclick()