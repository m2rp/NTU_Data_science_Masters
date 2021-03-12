#Question 4
'''
1) Initialize all vertices as not visited.
2) Do following for every vertex 'v'.
       (a) If 'v' is not visited before, call DFSUtil(v)
       (b) Print new line character

DFSUtil(v)
1) Mark 'v' as visited.
2) Print 'v'
3) Do following for every adjacent 'u' of 'v'.
     If 'u' is not visited, then recursively call DFSUtil(u)
'''
import numpy as np
from numpy import array

def DFS(r,c,num):
    print("DFS:{},{}".format(r,c))
    visited[r][c] = 1
    array[r][c] = num
    print("R{},C{}={}".format(r+1,c,visited[r+1][c]))
    if array[r-1][c] and not visited[r-1][c]: #Check on top
        DFS(r-1,c,num)
    if r!=row-1 and array[r+1][c]==1 and visited[r+1][c]==0: #Check on below
        DFS(r+1,c,num)
    if array[r][c-1] and not visited[r][c-1]: #Check on left
        DFS(r,c-1,num)
    if c != col-1 and array[r][c+1] and not visited[r][c+1]: #Check on right
        DFS(r,c+1,num)
    return

def printArr(arr):
    for row in array:
        print(row)

f = open('Question 4/input_question_4','r')
array=[]
for line in f:
    line = line.strip()
    array.append( [int(n) for n in line.split()] )
row = len(array)
col =  len(array[0])
print(row,col)
print("Original:")  
printArr(array)
print("\n")

visited = [[0]*col]*row
print("test",array[1][0], "visit", visited[1][0])
printArr(visited)
for r in range(row):
    for c in range(col):
        print("RC{},{} val{} visit{}".format(r,c,array[r][c],visited[r][c]))
        visited[r][c] = 0
contour_number = 1
for c in range(col):
    for r in range(row):
        print("RC{},{} val{} visit{}".format(r,c,array[r][c],visited[r][c]))
        if array[r][c]==1 and visited[r][c]==0:
            DFS(r,c,contour_number)
            contour_number += 1 
            printArr(array)
            print(contour_number)
            print("\n")
        #visited[r][c] = 1
        
        #else:
            #visited[r][c] = 1
print("final")
printArr(array)


