import math
import numpy as np
import random as random
import matplotlib.pyplot as plt
from matplotlib import colors


#The function below is to create the grid of our gas, the argument "n" is about number of particles we want inside our grid
#"dim" is an argument about the dimension of our grid, it's supposed to be a squared one, so the length of one axis is enough as input
def grid_gen(n,dim):
	cells=0
	grid1=np.zeros((dim,dim))
#The purpose of the loop below is to put gases particles in random position inside the grid, the while loop is to check if numbe of cells
#is the same as the input agument 'n', a and b are random integers and they express coordinates in our grid
#the "if" condition is to make sure that we're putting particles in empty place and not to replace another gas particle
# 0 means empty, 1 means the gas particle exists
#cells is to calculate the number of particle in the grid in the moment
	while cells != n:
		a=np.random.randint(dim)
		b=np.random.randint(dim)
		if grid1[a,b] == 0:
			grid1[a,b] = 1
			cells=cells+1
#the first two loops are to sweep the grid in the two axis, then for gives a direction for the existing particles (particles with value of 1)
	for i in range(dim):
		for j in range(dim):
			ij=np.random.random(1)
			if grid1[i,j]==1:
				if (ij <= 0.25):
					grid1[i,j]=2 #going right  
				elif (ij > 0.25) & (ij <= 0.5):
					grid1[i,j]=3  #going up          
				elif (ij > 0.5) & (ij <= 0.75):
					grid1[i,j]= 5 #going left 
				elif (ij > 0.75):
					grid1[i,j]= 7 #going down	
#the lines 	below are to create a visual figure of our system
	cmap = colors.ListedColormap(['white', 'black','black','black','black'])
	bounds = [0, 2,3,5,7,13]
	norm = colors.BoundaryNorm(bounds, cmap.N)
	grid = plt.imshow(grid1, interpolation='nearest', cmap=cmap,norm=norm)
	plt.show()
	return grid1


def what_is_next(grid,time):
	dim=int(math.sqrt(np.size(grid)))
#p is "wall ticks calculator"
	p=0
	print("The dimension is :  ",dim )
#beside the 2D loops, we added another loop that concern time(steps) to see the evolution of our system
	for t in range(time):
#grid_new is another grid that will have the value of the next step of our particles, it goes to zeros after every step 
		grid_new=np.zeros((dim,dim))
		for i in range(dim): #rules
			for j in range(dim):
#if particle is going right and collides with the edge of the grid, it will rebound
#if particle is going right and collides with a particle going left, one will go up and the other one will go down
#if particle is going right and there's nothing, then it will go right
				if grid[i,j]==2:
					if j==dim-1:
						grid_new[i,dim-1]=5
						p=p+1				
					elif grid[i,j+1]==5:
						grid_new[i,j]=3
						grid_new[i,j+1] =7
					else:
						grid_new[i,j+1]=grid[i,j]
#if particle is going left and collides with the edge of the grid, it will rebound
#if particle is going left and collides with a particle going right, one will go up and the other one will go down
#if particle is going left and there's nothing, then it will go left
				if grid[i,j]==5:
					if j == 0:
						grid_new[i,1] = 2
						p=p+1					
					elif grid[i,j-1]==2:
						grid_new[i,j]=7
						grid_new[i,j-1] =3
					else:
						grid_new[i,j-1]=grid[i,j]
#if particle is going up and collides with the edge of the grid, it will rebound
#if particle is going up and collides with a particle going down, one will go right and the other one will go left
#if particle is going up and there's nothing, then it will go up
				if grid[i,j]==3:
					if i == 0:
						grid_new[1,j]=7
						p=p+1					
					elif grid[i-1,j]==7:
						grid_new[i,j]=2
						grid_new[i-1,j]=5
					else:
						grid_new[i-1,j]=grid[i,j]
#if particle is going down and collides with the edge of the grid, it will rebound
#if particle is going down and collides with a particle going up, one will go right and the other one will go left
#if particle is going down and there's nothing, then it will go down
				if grid[i,j]==7:
					if i==dim-1:
						grid_new[dim-1,j]=3
						p=p+1					
					elif grid[i+1,j]==3:
						grid_new[i,j]=5
						grid_new[i+1,j]=2
					else:
						grid_new[i+1,j]=grid[i,j]
		grid=grid_new
	cmap = colors.ListedColormap(['white', 'black','black','black','black'])
	bounds = [0, 2,3,5,7,13]
	norm = colors.BoundaryNorm(bounds, cmap.N)
	grid = plt.imshow(grid, interpolation='nearest', cmap=cmap,norm=norm)
	plt.show()
	return p

#a function to calculate the average (further uses in the next one)
def average(array_of_values):
	return sum(array_of_values)/len(array_of_values)

#a function to repeat the process of the evolution in order to have different value of the same condition to have average value about wall ticks
def repeat_for_pressure(grid1,repeat):
	for r in range(repeat):
		pressure=[]
		what_is_next(grid1,time)
		pressure.append(p)
	return average(pressure)


print(what_is_next(grid_gen(100,100),10))