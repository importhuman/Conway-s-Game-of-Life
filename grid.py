import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
import numpy as np 
# import sys


#Force printing of entire array in terminal
# np.set_printoptions(threshold=sys.maxsize)

grid = np.zeros((51,51), dtype=np.int16) #Create 100*100 array of zeroes

def neighbors(x,y):
	#cell = grid[x,y]
	n_cells = [grid[x-1, y+1], grid[x, y+1], grid[x+1, y+1], 
				grid[x-1, y], grid[x+1, y], 
				grid[x-1, y-1], grid[x, y-1], grid[x+1, y-1]]
	return sum(n_cells)

grid[0:40, 0:35]=1

#print(grid)


#Rules
newgrid = grid.copy()
def updatefig(i):
	print(i)
	for x in range(50):
		for y in range(50):
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
	plt.imshow(newgrid, cmap='binary')

	

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
#plt.imshow(grid, cmap='binary')
ani = FuncAnimation(fig, updatefig, interval=100, repeat=False)
plt.show() #show the plot in a new window

print("done")
