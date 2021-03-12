def createMatrix(m,n):
    matrix = [[j+1 for i in range(n)] for j in range(m)]     
    return matrix

def findOperations(m,n,sum,current,path):
    current += m
    #print(m,n,current)
    if m==1 and n ==1:
        #print("End reached: " + path)
        if current == sum:
            operations = ''
            for x in path[::-1]:
                if x == 'L':
                    operations += 'R'
                elif x == 'U':
                    operations += 'D'
            print("Path found:" + operations)
        return  
    if m==1:
        path += 'L'
    
        findOperations(m,n-1,sum,current,path)
        return
    if n==1:
        path += 'U'

        findOperations(m-1,n,sum,current,path)
        return
    path += 'U'
    findOperations(m-1,n,sum,current,path)
    path = path[:-1]
    path += 'L'
    findOperations(m,n-1,sum,current,path)


if __name__ == '__main__':
    #matrix = createMatrix(3,3)
    #print(matrix)
    m = 90000
    n = 100000
    sum = 87127231192
    findOperations(m,n,sum,0,'')