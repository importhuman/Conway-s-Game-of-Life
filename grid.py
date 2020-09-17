import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
import numpy as np 
#import sys


#Force printing of entire array in terminal
#np.set_printoptions(threshold=sys.maxsize)

grid = np.zeros((51,51), dtype=np.int16) #Create 51*51 array of zeroes (index 0 to 50)

grid[15:30, 20:25]=1
grid[25:35, 10:15]=1


def neighbors(x,y):
	#cell = grid[x,y]
	n_cells = []
	#middle of the grid
	if x in range(1,50) and y in range(1,50): 
		n_cells = [grid[x-1, y+1], grid[x, y+1], grid[x+1, y+1], 
					grid[x-1, y], grid[x+1, y], 
					grid[x-1, y-1], grid[x, y-1], grid[x+1, y-1]]
	#first column edge
	if x==0 and y in range(1,50):
		n_cells = [grid[x, y+1], grid[x+1, y+1], 
				grid[x+1, y], grid[x, y-1], grid[x+1, y-1]]
	#last column edge
	if x==50 and y in range(1,50):
		n_cells = [grid[x-1, y+1], grid[x, y+1],
				grid[x-1, y], grid[x-1, y-1], grid[x, y-1]]
	#first row edge
	if y==50 and x in range(1,50):
		n_cells = [grid[x-1, y], grid[x+1, y], 
				grid[x-1, y-1], grid[x, y-1], grid[x+1, y-1]]
	#last row edge
	if y==0 and x in range(1,50):
		n_cells = [grid[x-1, y+1], grid[x, y+1], grid[x+1, y+1], 
				grid[x-1, y], grid[x+1, y]]
	#topleft corner
	if x==0 and y==50:
		n_cells = [grid[1,50], grid[0,49], grid[1,49]]
	#topright corner
	if x==50 and y==50:
		n_cells = [grid[49,50], grid[49,49], grid[50,49]]
	#bottomleft corner
	if x==0 and y==0:
		n_cells = [grid[0,1], grid[1,0], grid[1,1]]
	#bottomright corner
	if x==50 and y==0:
		n_cells = [grid[50,1], grid[49,0], grid[49,1]]
	return sum(n_cells)

#print(grid)

#Rules
newgrid = grid.copy()
def updatefig(i):
	#print(i) #Prints current iteration in terminal, for testing 
	for x in range(51):
		for y in range(51):
			if grid[x,y]==0:
				if neighbors(x,y)==3:
					newgrid[x,y]=1
			else:
				if neighbors(x,y)<2 or neighbors(x,y)>3:
					newgrid[x,y]=0

	def update_grid():
		global grid
		grid = newgrid.copy()

	update_grid()

	plt.cla() #clears previous plot, making animation faster
	
	#Placed in loop because doesn't work outside due to plt.cla()
	ax.set_xticklabels([])  
	ax.set_yticklabels([])
	ax.set_xticks([])
	ax.set_yticks([])
	
	plt.imshow(newgrid, cmap='binary')
	
fig, ax = plt.subplots()

#---------------This part doesn't work outside the loop because of plt.cla() in loop-------------
# #To get the current axes
# ax = plt.gca()
# #To make x and y axis tick labels invisible
# ax.set_xticklabels([])  
# ax.set_yticklabels([])
# #To make x and y axis ticks invisible
# ax.set_xticks([])
# ax.set_yticks([])
#-------------------------------------------------------------------------------

# print(grid)  #prints the array in terminal
#plt.imshow(grid, cmap='binary')
ani = FuncAnimation(fig, updatefig, interval=100, repeat=False)
plt.show() #show the plot in a new window

print("done")
