#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 00:34:24 2017

@author: shivamchaturvedi
"""

#The ratio of the areas of a circle and the square inscribing it is pi / 4. 
#In this six-part exercise, we will find a way to approximate this value.

#-------------------------------------------------

#2a
#Using the math library, calculate and print the value of pi / 4.


import math
from math import pi

x = math.pi/4

#print(x)

#-------------------------------------------------

#2b
#Using random.uniform, create a function rand() that generates a single float between -1 and 1.
#Call rand() once. So we can check your solution, we will use random.seed to fix the value called 
#by your function.


import random

random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.

def rand():
   return random.uniform(-1, 1)

rand()

#-------------------------------------------------

#2c
#The distance between two points x and y is the square root of the sum of squared differences along 
#each dimension of x and y. Create a function distance(x, y) that takes two vectors and outputs the 
#distance between them. Use your function to find the distance between (0,0) and (1,1).
#Print your answer.

def distance(x, y): #x,y are points 
    dist = math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 )#In our case here, the first point is x=(x[0],x[1])
    #and the second point is y=(y[0],y[1]). Therefore, the distance between two points is given by:
        #distance = sqrt((x[0]-y[0])^2+(x[1]-y[1])^2)
    return dist
    
print(distance((0,0),(1,1)))

#-------------------------------------------------

#2d
#distance(x, y) is pre-loaded from part 2c. Make a function in_circle(x, origin) that uses distance 
#to determine if a two-dimensional point falls within the the unit circle with a given origin. 
#That is, find if a two-dimensional point has distance <1 from the origin (0,0).
#Use your function to print whether the point (1,1) lies within the unit circle centered at (0,0).

def in_circle(x, origin = (0,0)): #Python, like other languages, provides support for default argument values, 
  #that is function arguments that can either be specified by the caller or left blank to automatically receive a predefined value.
  #In our case here we pre-defined the origin of the unit circle to be (0,0)
   return distance(x, origin) < 1

print(in_circle((1,1),(0,0))) #This results False as the point resides outside the unit circle. 
#if we choose another point, let say (0.5, 0.5), the resut would be true as the point sets inside the unit cirlce.

#As the origin is a pre-defined argument, we can exclude it from the function-calling syntax and write
#print(in_circle((1,1))) instead
#-------------------------------------------------

#2e
#The functions rand and in_circle are defined from previous exercises. 
#Using these functions, code is pre-entered that creates a list x of R=10000 
#two-dimensional points. Create a list of 10000 booleans called inside that are 
#True if and only if the point in x with that index falls within the unit circle. 
#Make sure to use in_circle!
#Print the proportion of points within the circle. 
#This proportion is an estimate of the ratio of the two areas!
    
R = 10000
x = [ (rand(), rand()) for i in range(R) ]
inside = [ in_circle(p) for p in x ]
print(sum(inside) / R)

#------

#another way to do it
R = 10000
x = []
inside = []

for i in range(R):
    point = [rand(), rand()]
    x.append(point)
    
for j in x:
    inside = [in_circle(j)] 
    
print(sum(inside)/R)
 
#-------------------------------------------------

#2f
#Note: inside and R are defined as in Exercise 2e. Recall the true ratio of the area of of the unit circle 
#to the area to the inscribing square is pi / 4.
#Find and print the difference between this value and your estimate from part 2e.


print( (math.pi / 4) - (sum(inside) / R) )