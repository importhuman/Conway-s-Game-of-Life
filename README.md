# Conway's Game of Life

This is an ongoing project to develop Conway's Game of Life in Python.

### What is the Game of Life?

Conway's Game of Life is a cellular automaton. It is a zero-player game, that is, its evolution is determined by its initial state and requires no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves.

The Game on Life occurs on an infinite 2D orthogonal grid of square cells. A cell can be live(populated) or dead(unpopulated). Each cell interacts with its 8 'neighbours', which are the cells adjacent to it (horizontally, vertically, and diagonally). 

The following rules are applied to each generation of cells (that is, for each iteration of the Game of Life):
1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

[(Source: Wikipedia)](https://en.wikipedia.org/wiki/Conway's_Game_of_Life)

### Current state of the project and using it

The game uses numpy and matplotlib to create a 51 * 51 array of zeroes (indices 0 to 50). Live and dead cells are denoted with 1s and 0s respectively. 

To set the initial state of the game, open `in_state.py` and enter the coordinates as you wish to, according to the following rules:

- 'x' and 'y' lists denote the x and y coordinates of the array/grid respectively
- 3 types of data can be placed into 'x' and 'y': individual points, lists, and tuples. All of them should be separated by commas.
- The project uses a zip function to create a combined list from 'x' and 'y'. Thus, the 1st item of 'x' is paired with 1st item of 'y', 2nd of 'x' with 2nd of 'y', and so on. Therefore, coordinates should be entered carefully.
- To input individual points, simply enter a single number from 0 to 50 in x and y.
- To input indiviual points with one of the same coordinate, use a list. Input the different coordinates as [a,b], and the corresponding coordinate as a single number (numbers should be from 0 to 50).
- To input a range, use a tuple. Input the range as (a,b) in the desired coordinate list. The 2nd coordinate should be greater than the 1st, i.e, b>a. The maximum range is (0,51).
- Do not combine tuples and lists with each other. Use them separately to assign different coordinates.
- 'x' and 'y' should have the same number of elements. Any extra elements in either list are ignored.

So, for example, the following code will create 3 isolated points:
```python
x = [1,2,3]
y = [4,8,13]
```

This will create 2 points with the same y coordinate:
```python
x = [[1,4]]
y = [2]
```
This will create 2 straight lines:
```python
x = [(1,20),(35,45)]
y = [10,40]
```


To use this project, fork and clone this repository, make the changes to `in_state.py` as you deem fit, run the `game.py` file, and have fun watching all sorts of patterns!

### Notes

- This project has only been tested for Python 3.8.2.
- The behaviour of cells is non-ideal at the edges and corners as of this stage. This is because the grid currently acts as a finite array, and not the infinite orthogonal grid it is ideally supposed to be.
- If you want to print out the complete array in the terminal, uncomment this segment of the code in the game.py file at the top
```python
#import sys
#np.set_printoptions(threshold=sys.maxsize)
```
and then add a `print` statement according to your requirements.