import math

a = float(input("შეიყვანეთ პირველი გვერდი: "))
b = float(input("შეიყვანეთ მეორე გვერდი: "))
c = float(input("შეიყვანეთ მესამე გვერდი: "))

perimeter = a + b + c

s = perimeter / 2  
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f"პერიმეტრი: {perimeter}")
print(f"ფართობი: {area:.2f}")