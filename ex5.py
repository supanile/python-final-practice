def factorial(n):
    if n < 0:
        print("n must be >= 0 input try again")
        return None

    fact = 1
    for i in range(1,n + 1):
        fact *= i

    return fact

while True:
    n = int(input("Enter factorial(n): "))
    
    if n >= 0:
        result = factorial(n)
        if result is not None:
            print(f"factorial({n}): {result:,}")
            break
    else:
        print("n must be >= 0. Input try again.")

print("End program!")
