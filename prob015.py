# coding=utf-8
# Lattice paths
# Problem 15

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

def gridout(grid):
  for row in grid:
    print row

def routes (nodes):
  nodesperside = nodes + 1   # Problem says side is 2x2, which means 3 nodes per side
  #print "in routes with nodesperside =",nodesperside
  grid = [ [ 0 for i in range(nodesperside) ] for j in range(nodesperside) ]
  for row in grid:
    row[len(row)-1] = 1
  for cell in range(0,len(row)-1):
    grid[len(grid)-1][cell] = 1
  grid[nodesperside-1][nodesperside-1] = 0

  # gridout(grid)

  for row in range(nodesperside-2,-1,-1):
    #print "row:",row
    for col in range(nodesperside-2,-1,-1):
      #print "col:",col
      grid[row][col] = grid[row][col+1] + grid[row+1][col]

  print "A grid of size",nodes,"x",nodes,"has",grid[0][0],"routes."

  # gridout(grid)

side = 2
routes(side)

side = 3
routes(side)

side = 20
routes(side)
