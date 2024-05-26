def compound_interest(p, r, n, t):
    return p * ((1 + (r / n)) ** (n * t))

def main():
    p = float(input("Enter principal amount: "))
    r = float(input("Enter interest rate: "))
    n = int(input("Enter number of times interest is compounded per year: "))
    t = int(input("Enter number of years: "))

    if p <= 0 or r < 0 or n <= 0 or t <= 0:
        print("Invalid input. Please enter positive values for principal amount, interest rate, interest time, and number of years.")
    else:
        result = compound_interest(p, r, n, t)
        formatted_result = round(result, 2)
        print("Compound interest:", formatted_result)

main()
