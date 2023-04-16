# LayeredEcard 🖌

## Description
This is a Python program that draws 3D-like images using the Turtle library. 

![Layered Ecard](https://github.com/joet-dev/LayeredEcard/blob/master/blockArt.png?raw=true)

**How it works**

The interesting thing about the program is that it generates the models from "model data files" which are just nested lists containing colour prompts and cube locations. 

The model data file contains:
 -the start location of the environment (the first cube 'layer' that is drawn for the model to stand on)
 -the size of the environment
 -the colour of the environment
 -the data (colour and location) that produces the model
