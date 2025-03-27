import random
random.seed( 4 )
print("Random number with seed 4 : ", random.random()) #will generate a random number 
#if you want to use the same random number once again in your program
random.seed( 4 )
random.random()   # same random number as before