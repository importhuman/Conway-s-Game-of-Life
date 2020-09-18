#Enter data as x =  a,b,c and y = d,e,f. x and y should have values from 0 to 10.
#For multiple points with same corresponding coordinate, enter them as a list [a,b,c]
#To specify a range, enter points as a tuple (a,b). b should be greater than a.
#Tuples can have 2nd values upto 11.
#Do not combine tuples and lists with each other, use only one at a time. All individual points, tuples, lists should be separated by commas

# 'x' and 'y' lists denote the x and y coordinates of the array/grid respectively
# 3 types of data can be placed into 'x' and 'y': individual points, lists, and tuples. All of them should be separated by commas.
# The project uses a zip function to create a combined list from 'x' and 'y'. Thus, the 1st item of 'x' is paired with 1st item of 'y', 2nd of 'x' with 2nd of 'y', and so on. Therefore, coordinates should be entered carefully.
# To input individual points, simply enter a single number from 0 to 50 in x and y.
# To input indiviual points with one of the same coordinate, use a list. Input the different coordinates as [a,b], and the corresponding coordinate as a single number (numbers should be from 0 to 50).
# To input a range, use a tuple. Input the range as (a,b) in the desired coordinate list. The 2nd coordinate should be greater than the 1st, i.e, b>a. The maximum range is (0,51).
# Do not combine tuples and lists with each other. Use them separately to assign different coordinates.
# 'x' and 'y' should have the same number of elements. Any extra elements in either list are ignored.

x = [(10,20), 20]
y = [10,(20,30)]