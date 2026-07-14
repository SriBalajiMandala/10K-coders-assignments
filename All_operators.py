#1. Arithmetic Operators
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

#2. Comparison (Relational) Operators
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#3. Assignment Operators
x = 10

x += 5
print(x)

x -= 2
print(x)

x *= 3
print(x)

x /= 2
print(x)

x //= 2
print(x)

x %= 3
print(x)

x **= 2
print(x)

#4. Logical Operators
a = True
b = False

print(a and b)
print(a or b)
print(not a)

#5. Bitwise Operators
a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)

#6. Membership Operators
fruits = ["apple", "banana", "mango"]

print("apple" in fruits)
print("grapes" in fruits)

print("apple" not in fruits)
print("grapes" not in fruits)

#7. Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)

print(a is not c)

#8. Conditional (Ternary) Operator
a = 10
b = 20

result = "a is greater" if a > b else "b is greater"
print(result)