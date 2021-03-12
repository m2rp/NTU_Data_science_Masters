#fill the largest colour alternate which is blue
$fill the second largest colour (white) between blue
#fill the third colour (yellow) between green
#fill the yellow and red between green
#put 1 green at (1,1)
#put 1 blue at (64,64)



blue = 1451
white = 1072
green = 977
yellow = 457
red = 139

grid = [ [0]*64 for i in range(64)]

for i in range(64):
    for j in range(64):
        grid[i][j] = 0

i = 0
j = 0
k = 0
while (blue > 0):
    grid[i][j] = 1 
    j += 2
    if j > 63:
        i += 1
        if k==0:
            j = 1
            k=1
        else:
            j = 0;
            k=0
    blue -= 1

while (yellow > 0):
    grid[i][j] = 4 
    j += 2
    if j > 63:
        i += 1
        if k==0:
            j = 1
            k=1
        else:
            j = 0;
            k=0
    yellow -= 1

while (red > 0):
    grid[i][j] = 5 
    j += 2
    if j > 63:
        i += 1
        if k==0:
            j = 1
            k=1
        else:
            j = 0;
            k=0
    red -= 1
    
i = 0
j = 1
k = 1
while (white > 0):
    grid[i][j] = 2 
    j += 2
    if j > 63:
        i += 1
        if k==0:
            j = 1
            k=1
        else:
            j = 0;
            k=0
    white -= 1

while (green > 0):
    if (i > 63):
        break
    grid[i][j] = 3 
    j += 2
    if j > 63:
        i += 1
        if k==0:
            j = 1
            k=1
        else:
            j = 0;
            k=0
    green -= 1

grid[63][63] = 1
grid[0][0] = 3

for l in range(64):
    print(grid[l])

            
