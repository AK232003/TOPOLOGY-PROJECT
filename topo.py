# import sympy 
#from sympy import * 
import sympy as sym

print("number of vertices: ")
num_ver = int(input())
print("number of edges: ")
num_edg = int(input())
print("number of faces: ")
num_fac = int(input())

ver = []
edges = []
faces =[]

print("Enter the vertices: ")
for i in range(0, num_ver):
    j = int(input())
    ver.append(j)

print("Enter the edges: ")
for i in range(0, num_edg):
    temp=[]
    v1 = int(input())
    v2 = int(input())
    temp.append(v1)
    temp.append(v2)
    edges.append(temp)

print(edges)

img_space = []
#count = 0
#print(img_space)
for i in range(0, num_ver):
    temp1=[]
    for j in range(0, num_edg):
        #print(edges[i][0], edges[i][1], i, j)
        if(edges[j][0] == (i+1)):
            #print("Hello")
            temp1.append(-1)
            #count+=1
            #print(temp1)
        elif(edges[j][1] == i+1):
            temp1.append(1)
            #print(temp1)
        else:
            temp1.append(0)
            #print(temp1)
        #print(img_space)
    img_space.append(temp1)

print(img_space)

rank = sym.Matrix(img_space).rank()
#A = RREF
#print(RREF)
#print(A[0])

betti_0 = num_ver - rank
print(betti_0)