import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
import numpy as np 
# import time
# import sys


#Force printing of entire array in terminal
# np.set_printoptions(threshold=sys.maxsize)

grid = np.zeros((11,11), dtype=np.int16) #Create 100*100 array of zeroes

def neighbors(x,y):
	#cell = grid[x,y]
	n_cells = [grid[x-1, y+1], grid[x, y+1], grid[x+1, y+1], 
				grid[x-1, y], grid[x+1, y], 
				grid[x-1, y-1], grid[x, y-1], grid[x+1, y-1]]
	return sum(n_cells)

grid[0:5,0:5]=1

#Rules

def updatefig(i):
	newgrid = grid.copy()
	for x, y in zip(range(10), range(10)):
		if newgrid[x,y]==1:
			if neighbors(x,y)<2:
				newgrid[x,y]=0
			elif neighbors(x,y)>3:
				newgrid[x,y]=0
		else:
			if neighbors(x,y)==3:
				newgrid[x,y]=1
	# 		#time.sleep(0.1)
	return newgrid
	

#PROBLEM SEEMS TO BE WITH NEWGRID. IT'S NOT RETURNING AS AN ARRAY.


fig, ax = plt.subplots()

#To get the current axes
ax = plt.gca()

#To make x and y axis tick labels invisible
ax.set_xticklabels([])  
ax.set_yticklabels([])

#To make x and y axis ticks invisible
ax.set_xticks([])
ax.set_yticks([])

# print(grid)  #prints the array in terminal

ani = FuncAnimation(fig, updatefig, interval=100)

#plt.imshow(grid, cmap='binary') #create grid, 0=white, 1=black #DO THIS AFTER MODIFYING THE ARRAY TO REFLECT CHANGES
plt.show() #show the plot in a new window


print("done")

# ---------------Old code------------------------

# plt.plot([1,2,3,4],[1,4,2,3])
# plt.grid(True)
# plt.show()


#Make a grid
# plt.grid(b=None, which='both', axis='both', linestyle='-', linewidth=1)


# #Make the tick labels invisible
# ax = plt.gca()
# ax.set_xticklabels([])
# ax.set_yticklabels([])

# plt.show()
