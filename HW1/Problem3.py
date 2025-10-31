n = int(input("Enter number: "))

if n <= 0 or n >= 100:
    print("Please enter a natural number less than 100.")
else:
    fibonacci = []
    for i in range(n):
        if i == 0:
            fibonacci.append(0)
        elif i == 1:
            fibonacci.append(1)
        else:
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

    print(fibonacci)
