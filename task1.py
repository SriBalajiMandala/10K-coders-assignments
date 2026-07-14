#1.max number
def maximum(a, b):
    if a > b:
        return a
    else:
        return b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Maximum number is:", maximum(num1, num2))

#2.Check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))
print(check_even_odd(number))

#Factorial of a number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))

#IS prime number
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime Number")
else:
    print("Not a Prime Number")


#list sum
def list_sum(numbers):
    total = 0

    for i in numbers:
        total += i

    return total

lst = [10, 20, 30, 40, 50]

print("Sum =", list_sum(lst))

#String reverse
def reverse_string(text):
    return text[::-1]

name = input("Enter a string: ")

print("Reversed String:", reverse_string(name))

#count vowels
def count_vowels(text):
    count = 0

    vowels = "aeiouAEIOU"

    for ch in text:
        if ch in vowels:
            count += 1

    return count

word = input("Enter a string: ")

print("Number of vowels:", count_vowels(word))