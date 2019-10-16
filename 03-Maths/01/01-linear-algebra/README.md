# Foreword
In this challenge, we will learn how to manipulate matrices and how to implement basic operations such as addition, matrix product, dot product,...

## 🔥 Warm-up

A matrix can be seen as an array of arrays. For example, we could represent a matrix A (3x3):
`
A = [[1,2,4],[1,1,1],[1,2,8]]
`
To access an element, we first indicate the row and then the column (remember, in Python indices start at 0!).

So if you want the retrieve "8" from this matrix, you should compute:
`A[2][2]`

For this exercise, you have to implement some basic functions (in `basic_functions.py` file). If you want to use some of them in the next exercise(s), feel free to do so. When coding, it's always a good idea to re-use work you've already done.

Quick reminder : `from basic_functions import *` will import all functions from the module basic_functions.

## 1. Addition of 2 matrices
In this exercise, you will implement the function `addition_2_matrices(matrix_1, matrix_2)` which should return the sum of matrix_1 and matrix_2.
`
matrix_r(i,j) = matrix_1(i,j) + matrix_2(i,j)
`

If the dimensions of the 2 matrices are not consistent, you should return a IndexError and print a message on the console.

If you need more information about matrix addition, [have a look at this article](https://en.wikipedia.org/wiki/Matrix_addition)

## 2. Transpose of a Matrix
The transpose of a matrix is an operator which flips a matrix over its diagonal that is it switches the row and column indices of the matrix by producing another matrix.

What does that mean? The i-th row, j-th column element of A_t (transpose of A) is the j-th row, i-th column element of A:
`A_t_ij = A_ji`

In this challenge, you will have to implement the function transpose() to return the transpose of a Matrix.

## 3. Matrix Multiplication
Now, let's get serious. We will implement manually the "Matrix Multiplication" inside `product.py`. As a reminder, if the size of A is (m, n) and B is (n, p), then C will be (m, p) and
`C(i,j) = A(i,0)*B(0,j) + A(i,1)*B(1,j) +...+ A(i,n)*B(n,j)`

Again, if you want more explanation about how to compute Matrix Multiplication, you could [have a look here](https://en.wikipedia.org/wiki/Matrix_multiplication)
