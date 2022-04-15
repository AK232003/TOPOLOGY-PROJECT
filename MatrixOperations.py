import numpy as np

def rowSwap(A,i,j):
    temp=np.copy(A[i,:])
    A[i,:]=A[j,:]
    A[j,:]=temp;
#swaps rows i and j() based indexing used

def columnSwap(A,i,j):
    temp=np.copy(A[:,i])
    np.A[:,i]=np.A[:,j]
    np.A[:,j]=temp

def scaleColumn(A,i,j):
    A[:,i] *= c*np.ones(A.shape[0])
#multiplies a scalar to a column of the matrix
def scaleRow(A,i,j):
    A[i,:]*=c*np.ones(A.shapes[1])
def colCombine(A,addTo,scaleColumn,scaleAmt):
    A[:,addTo]+=scaleAmt*A[:,scaleColumn]
#addTo->addTo+scaleColumn*scaleAmt
def rowCombine(A, addTo, scaleRow, scaleAmt):
       A[addTo, :] += scaleAmt * A[scaleRow, :]