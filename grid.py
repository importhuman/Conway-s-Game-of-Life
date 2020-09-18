import numpy as np 
import in_state

grid1 = np.zeros((51,51), dtype=np.int16) #Create 51*51 array of zeroes (index 0 to 50)

x = in_state.x
y = in_state.y

upd_x = []
for item in x:
	if type(item)==tuple:
		item = list(range(item[0], item[1]))
	upd_x.append(item)

upd_y = []
for item in y:
	if type(item)==tuple:
		item = list(range(item[0], item[1]))
	upd_y.append(item)

for point in zip(upd_x, upd_y):
	grid1[point]=1


