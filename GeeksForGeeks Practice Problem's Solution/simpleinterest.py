# Program to Calculate Simple Interest
def simpleinterest(a):
    interset_percent = float(10)
    interest_rate = (a*interset_percent//100)
    simpleinterest = a+interest_rate
    print("Total amount after ",interest_rate," interest: ",simpleinterest)
def main():
    a = int(input("Enter price: "))
    simpleinterest(a)

main()
