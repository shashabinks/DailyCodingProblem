# Problem: Given an array of integers, return a new array such that each element at index i of the new array is the product of all the
# numbers in the original array except the one at i

def product(arr,n):
    p = []


    L , R , psum = [0]*n,[0]*n,[0]*n

    L[0] = 1
    for i in range(1,n):
        L[i] = arr[i-1] * L[i-1]

    R[n-1] = 1

    for i in reversed(range(n-1)):
        R[i] = arr[i+1] * R[i+1]


    for i in range(n):

        psum[i] = L[i] * R[i]

    print(psum)

arr = [1,2,3,4,5]
n   = len(arr)
product(arr,n)
