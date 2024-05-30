
def printAscii(n):
    for i in n:
        print(f"Ascii of {i} is: ",ord(i))

def main():
    a = str(input("Enter character: "))
    printAscii(a)
main()
