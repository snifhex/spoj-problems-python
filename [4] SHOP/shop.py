import numpy as np

class Graph:

    def __init__(self, n_v, src, dest, g):
        self.v = n_v
        self.s = src
        self.d = dest
        self.g = g


    def findShortestPath(self):

        distances = [] #from source vertex
        visited = [False] * self.v #keep track of visited vertices

        for i in range(self.v): #total vertices
                distances.append(float("inf"))
        distances[self.s] = 0 #source vertex to source vertex is 0 distance
        #select minimum, greedy approach


        for x in range(self.v):
            minimum = float("inf")
            for i in range(len(distances)):
                if visited[i] == False and distances[i] < minimum:
                    minimum = distances[i]
                    min_idx = i
            visited[min_idx] = True
    
            if minimum == float("inf"):
                flag = True
                break
    
            for vert in range(len(distances)):
                if not visited[vert]:
                    if distances[vert] > distances[min_idx]+self.g[min_idx][vert] \
                            and self.g[min_idx][vert] != 0:
                        distances[vert] = distances[min_idx]+self.g[min_idx][vert]
            if self.d == min_idx:
                break
        return distances[self.d]-1


    def printShortestPath(self):
        print(self.findShortestPath())

#g =  [
#        [0, 4, 0, 0, 0, 0, 0, 8, 0], 
#        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
#        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
#        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
#        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
#        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
#        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
#        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
#        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
#    ]
#
#gr = Graph(9,0,5,g)
#gr.printShortestPath()


cnt = 0
while True:
    if cnt:
        _ = input() #blank link
        c, r = map(int, input().split(' '))
    else:
        c, r = map(int, input().split(' '))        
    if c == r and r == 0:
        break
    arr = []
    for i in range(r):
        x = []
        string = input()
        j = 0
        for char in string:
            if char == 'S' or char == 'D' or char == 'X':
                if char == 'S':
                    src = c*i + j
                    x.append('0')
                elif char == 'D':
                    dest = c*i + j
                    x.append('1')
                else:
                    x.append('0')
            else:
                x.append(char)
            j += 1
        arr.append(x)

    g = [] #dimensions is r*c * r*c (adjacency matrix) 
    for i in range(r*c):
        x = []
        for j in range(r*c):
            x.append(0)
        g.append(x)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i==0 and j==0:
                #down
                g[c*i + j][c*(i+1) + j] = int(arr[i+1][j])
                #right
                g[c*i + j][c*i + j+1] = int(arr[i][j+1])
            elif i==0 and j!=0 and j!=c-1:
                #down
                g[c*i + j][c*(i+1) + j] = int(arr[i+1][j])
                #right
                g[c*i + j][c*i + j+1] = int(arr[i][j+1])
                #left
                g[c*i + j][c*i + j-1] = int(arr[i][j-1])

            elif i==0 and j==c-1:
                #down
                g[c*i + j][c*(i+1) + j] = int(arr[i+1][j])
                #left
                g[c*i + j][c*i + j-1] = int(arr[i][j-1])
            elif i==r-1 and j==0:
                #up
                g[c*i + j][c*(i-1) + j] = int(arr[i-1][j])
                #right
                g[c*i + j][c*i + j+1] = int(arr[i][j+1])
            elif i==r-1 and j!=0 and j!=c-1:
                #up
                g[c*i + j][c*(i-1) + j] = int(arr[i-1][j])
                #left
                g[c*i + j][c*i + j-1] = int(arr[i][j-1])
                #right
                g[c*i + j][c*i + j+1] = int(arr[i][j+1])
            elif i==r-1 and j==c-1:
                #up
                g[c*i + j][c*(i-1) + j] = int(arr[i-1][j])
                #left
                g[c*i + j][c*i + j-1] = int(arr[i][j-1])
                
            elif j==0:
                #up
                g[c*i + j][c*(i-1) + j] = int(arr[i-1][j])
                #down
                g[c*i + j][c*(i+1) + j] = int(arr[i+1][j])
                #right
                g[c*i + j][c*i + j+1] = int(arr[i][j+1])
            elif j==c-1:
                #up
                g[c*i + j][c*(i-1) + j] = int(arr[i-1][j])
                #down
                g[c*i + j][c*(i+1) + j] = int(arr[i+1][j])
                #left
                g[c*i + j][c*i + j-1] = int(arr[i][j-1])
            else:
                #up
                g[c*i + j][c*(i-1) + j] = int(arr[i-1][j])
                #down
                g[c*i + j][c*(i+1) + j] = int(arr[i+1][j])
                #left
                g[c*i + j][c*i + j-1] = int(arr[i][j-1])
                #right
                g[c*i + j][c*i + j+1] = int(arr[i][j+1])
    gr = Graph(r*c,src,dest,g)
    gr.printShortestPath()
    cnt += 1
