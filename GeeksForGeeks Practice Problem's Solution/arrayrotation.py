# Function To rotate array by 1 element
from random import randint
def array_rotation(arr):
    tmp = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr)-1] = tmp
    return arr
def main():
    arr = [randint(1,20) for i in range(20)]
    print(arr)
    print(array_rotation(arr))
main()
