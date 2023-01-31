#Day 6 Project
# Algorithm: follow along the right edge of the wall.

# If the right side is clear,

# Then, continue going right until it's no longer clear at which point it should just go straight. 

# If you can't go straight and you can't go right, then the last option is to turn left.
    
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# while front_is_clear():
#     move()
# turn_left()

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move() #achieves a move with "right direction"
#     elif front_is_clear(): #check if front is clear
#         move() # if condition is true, then move forward
#     else:
#         turn_left()# if front and right is not clear, then turn left.

#Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json