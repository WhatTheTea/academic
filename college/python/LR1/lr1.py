# Part 1
print("привіт світ!")

firstName = input("Введіть ваше ім'я: ")
lastName = input("Введіть ваше прізвище: ")

print("Привіт, ", firstName, lastName, end='\n\n')

# Part 2
import math

up = 34 + 6**2 * math.sqrt(225)
down = math.cos(math.radians(60)) * 14
res = (up/down)**2

print("result: ",res, end='\n\n')

# Part 3 | 8 variant
print((math.sqrt(44) - 3)*24 + 3**5, end='\n\n')
print("9x^2 - 24x + 16 = 0")
a = 9.0
b = -24.0
c = 16.0
discriminant = (b**2) - (4*a*c)
x1 = (-b + math.sqrt(discriminant)) / (2*a)
x2 = (-b - math.sqrt(discriminant)) / (2*a)

print("x1: ", x1)
print("x2: ", x2)