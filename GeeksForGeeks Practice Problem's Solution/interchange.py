# Function To Swap The last and First element
from random import randint
def swap_last(arr):
    arr[0],arr[-1] = arr[-1],arr[0]
    return arr
def main():
    arr = [randint(0,20) for i in range(20)]
    print(arr)
    print(swap_last(arr))
main()