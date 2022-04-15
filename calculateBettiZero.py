import simultaneousReduce
import numpy
def numPivotCols(A):
    z = numpy.zeros(A.shape[0])
    return [numpy.all(A[:, j] == z) for j in range(A.shape[1])].count(False)
 
def numPivotRows(A):
   z = numpy.zeros(A.shape[1])
   return [numpy.all(A[i, :] == z) for i in range(A.shape[0])].count(False)

def bettiNumber(d_k, d_kplus1):
    A, B = numpy.copy(d_k), numpy.copy(d_kplus1)
    simultaneousReduce(A, B)
    finishRowReducing(B)
        
    dimKChains = A.shape[1]
    kernelDim = dimKChains - numPivotCols(A)
    imageDim = numPivotRows(B)
        
    return kernelDim - imageDim