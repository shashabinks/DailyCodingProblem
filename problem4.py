# Problem
# Given an array of integers, find the first missing positive integer in linear time and constant space



p = []
n = []

arr=[3, 4, -1, 1]

end = len(arr)



def fill_arr():
    for i in range(end):
        if arr[i] > 0:
            p.append(arr[i])
        else:
            n.append(arr[i])

def


fill_arr()



print(p)
