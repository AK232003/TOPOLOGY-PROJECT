import sympy as sym
import numpy as np
import scipy.linalg.interpolative as sli
import time


def readfile(filename):
    f = open(filename, "r+");
    line = (f.readline());
    list_ver_edg_fac = line.split(' ');
    num_ver = int(list_ver_edg_fac[0]); 
    print("The number of vertices are: ", num_ver);
    num_edg = int(list_ver_edg_fac[1]);
    print("The number of edges are: " ,num_edg);
    num_fac = int(list_ver_edg_fac[2]);
    print("The number of faces are: " ,num_fac);

    
    ver = []
    edges = []
    faces =[]
    # coords = []

    for i in range(0, num_ver):
        j = f.readline()
        # coords.append(j)

    for i in range(0, num_ver):
        ver.append(i+1);

    for i in range(0, num_edg):
        edge = f.readline();
        edge_1 = list(map(int, edge.split(' ')))
        edges.append(edge_1)
    Return = []
    Return.append(num_ver)
    Return.append(num_edg)
    Return.append(edges)
    return Return


def image_space(edges, num_ver, num_edg):
    img_space = []
    for i in range(0, num_ver):
        
        temp1=[0]*num_edg
        a=False
        b=False
        for j in range(0, num_edg):
            if(edges[j][0] == (i+1)):
                temp1[j]=-1
                a=True

            elif(edges[j][1] == i+1):
                temp1[j]=1
                b=True
            elif(a==True and b==True):
                continue

        img_space.append(temp1)
    return img_space

def calculate_betti_0(img_space, num_ver):
    begin=time.time()
    rank_matrix = np.array(img_space)
    rank=np.linalg.matrix_rank(rank_matrix)
    betti_0 = num_ver - rank

    print("==========")
    print('| \N{GREEK SMALL LETTER BETA}\N{SUBSCRIPT ZERO} =',betti_0,'|')
    print("==========")
    end=time.time()
    print("total execution time(in sec) = ",end-begin)

def main():
    file_name = input("Enter the filename for reading the data\n")
    Return_list = readfile(file_name)
    num_ver = Return_list[0]
    num_edg = Return_list[1]
    edges_list = Return_list[2]
    img_space_list = image_space(edges_list, num_ver, num_edg)
    calculate_betti_0(img_space_list, num_ver)

main()