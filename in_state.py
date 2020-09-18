import numpy as np 

#Enter data as x =  a,b,c and y = d,e,f. x and y should have values from 0 to 10.
#For multiple points with same corresponding coordinate, enter them as a list [a,b,c]
#To specify a range, enter points as a tuple (a,b). b should be greater than a.
#Tuples can have 2nd values upto 11.
#Do not combine tuples and lists with each other, use only one at a time. All individual points, tuples, lists should be separated by commas

grid = np.zeros((51,51), dtype=np.int16) #Create 51*51 array of zeroes (index 0 to 50)
x = (1,20),(35,45)
y= 10,40


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
	grid[point]=1


