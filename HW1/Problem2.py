number = int(input("Enter number: "))

if number <= 0 or number >= 1000:
    print("Please enter a natural number less than 1000.")
else:
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)

    print(" ".join(map(str, divisors)))
