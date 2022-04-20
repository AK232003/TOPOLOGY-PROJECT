import string
import sympy as sym
import numpy as np
import scipy.linalg.interpolative as sli
import time
begin=time.time()

def readfile(filename):
    f = open(filename, "r+");
    line = (f.readline());
    list_ver_edg_fac = line.split(' ');
    num_ver = int(list_ver_edg_fac[0]); 
    print("The number of vertices are: " + str(num_ver));
    num_edg = int(list_ver_edg_fac[1]);
    print("The number of edges are: " + str(num_edg));
    num_fac = int(list_ver_edg_fac[2]);
    print("The number of faces are: " + str(num_fac));

    #print(type(num_ver));
    ver = []
    edges = []
    faces =[]
    coords = []
    #print("Enter the vertices: ")
    for i in range(0, num_ver):
        j = f.readline()
        coords.append(j)

    #print(coords)
    #    coords.append(j)

    for i in range(0, num_ver):
        ver.append(i+1);

    #print("The vertices are: " + str(ver))

    #print("Enter the edges: ")
    for i in range(0, num_edg):
        edge = f.readline();
        edge_1 = list(map(int, edge.split(' ')))
        edges.append(edge_1)
    Return = []
    Return.append(num_ver)
    Return.append(num_edg)
    Return.append(edges)
    return Return
#print(edges)

def image_space(edges, num_ver, num_edg):
    #print("Hello\n")
    img_space = []

    for i in range(0, num_ver):
        temp1=[0]*num_edg
        # temp1=[]
        a=False
        b=False
        for j in range(0, num_edg):
            if(edges[j][0] == (i+1)):
                # temp1.append(-1)
                temp1[j]=-1
                a=True

            elif(edges[j][1] == i+1):
                # temp1.append(1)
                temp1[j]=1
                b=True
            elif(a==True and b==True):
                continue
            # else:
                # temp1.append(0)

        img_space.append(temp1)
    #print("Hello\n")
    return img_space

# print()
#print(img_space)
# for i in range(num_ver):
#     for j in range(num_edg):
#         if(img_space[i][j] >= 0):
#             print("  ", img_space[i][j], end = " ")
#         else:
#             print(" ",img_space[i][j], end = " ")
#     print()
def calculate_betti_0(img_space, num_ver):
    rank_matrix = np.array(img_space)
    # rank = sym.Matrix(img_space).rank()
    rank=np.linalg.matrix_rank(rank_matrix)
    #rank = sli.estimate_rank(rank_matrix, eps=1e-10)
    print("Rank: " + str(rank))
    betti_0 = num_ver - rank

    print("==========")
    print('| \N{GREEK SMALL LETTER BETA}\N{SUBSCRIPT ZERO} =',betti_0,'|')
    print("==========")
    end=time.time()
    print("total execution time(in sec) = ",end-begin)

def main():
    file_name = str(input())
    Return_list = readfile(file_name)
    num_ver = Return_list[0]
    #print(type(num_ver))
    #print(Return_list[0])
    num_edg = Return_list[1]
    edges_list = Return_list[2]
    img_space_list = image_space(edges_list, num_ver, num_edg)
    calculate_betti_0(img_space_list, num_ver)

main()