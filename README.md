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

Currently, the game comprises of a single file, grid.py. It uses numpy and matplotlib to create a 51 * 51 array of zeroes (indices 0 to 50). Live and dead cells are denoted with 1s and 0s respectively. To enter the initial state of the game, give a value of 1 to the cells you want, like this:

```python
grid[x,y]=1
```

x and y denote the x and y coordinates in the array respectively. These can be individual points, such as
 ```python
 grid[4,5]=1
 ```

but doing this will produce a single live cell in the initial state that dies in the next iteration, unless placed specifically to continue the game. Thus, for starting out, simple lines and quadrilaterals are suggested, such as
```python
grid[0:50, 25]=1 #produces a straight line
```
or
```python
grid[20:40, 20:40]=1 #produces a square
```

You can also set up multiple unconnected points and figures in the array.
```python
grid[15:30, 20:25]=1
grid[25:35, 10:15]=1
```

To use this project, fork and clone this repository, make the changes to the initial state as you deem fit, run the grid.py file, and have fun watching all sorts of patterns!

### Notes

- This project has only been tested for Python 3.8.2.
- Modify the grid before the 
```python
newgrid = grid.copy() 
```
line. Changing it afterwards leads to different behaviour of the initial state as of this stage. 
- The behaviour of cells is non-ideal at the edges and corners as of this stage. This is because the grid currently acts as a finite array, and not the infinite orthogonal grid it is ideally supposed to be.
- If you want to print out the complete array in the terminal, uncomment this segment of the code at the top
```python
#import sys
#np.set_printoptions(threshold=sys.maxsize)
```
and then add a `print` statement according to your requirements.