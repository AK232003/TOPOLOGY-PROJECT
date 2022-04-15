def simultaneousReduce(A, B):
    if A.shape[1] != B.shape[0]:
      raise Exception("Matrices have the wrong shape.")
 
    numRows, numCols = A.shape # col reduce A
 
    i,j = 0,0
    while True:
      if i >= numRows or j >= numCols:
         break
 
      if A[i][j] == 0:
         nonzeroCol = j
         while nonzeroCol < numCols and A[i,nonzeroCol] == 0:
            nonzeroCol += 1
 
         if nonzeroCol == numCols:
            j += 1
            continue
 
         colSwap(A, j, nonzeroCol)
         rowSwap(B, j, nonzeroCol)
 
      pivot = A[i,j]
      scaleCol(A, j, 1.0 / pivot)
      scaleRow(B, j, 1.0 / pivot)
 
      for otherCol in range(0, numCols):
         if otherCol == j:
            continue
         if A[i, otherCol] != 0:
            scaleAmt = -A[i, otherCol]
            colCombine(A, otherCol, j, scaleAmt)
            rowCombine(B, j, otherCol, -scaleAmt)
 
      i += 1; j+= 1
 
    return A,B