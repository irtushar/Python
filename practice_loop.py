# Problem -1
# multiplication table

# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(n, "x", i, "=", n*i)

# Problem -2
# factorial of a number

# n = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
# print("Factorial of", n, "is", factorial)

# Problem -3
# Fibonacci series

# n = int(input("Enter a number: "))
# a = 0
# b = 1
# for i in range(n):
#     print(a, end=' ')
#     a = b
#     b = a + b
# print()

# Problem -4
# counting digits in a number
# method 1

# n = int(input("Enter a number: "))
# count = 0
# while n > 0:
#     count += 1
#     n = n // 10
# print("Number of digits:", count)

# method 2
# n = input("Enter a number: ")
# print("Number of digits:", len(n))

# Problem -5
# find armstrong number
# method 1

# n = int(input("Enter a number: "))
# sum = 0
# temp = n
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** 3
#     temp //= 10
# if sum == n:
#     print(n, "is an Armstrong number")
# else:
#     print(n, "is not an Armstrong number")

# method 2
# a = input("Enter a number: ")
# n = len(a)
# sum = 0
# for i in a:
#     sum += int(i) ** n
# if sum == int(a):
#     print(a, "is an Armstrong number")  
# else:
#     print(a, "is not an Armstrong number")

# Problem -6
# integer number reverse

# a = int(input("Enter a number: "))
# reverse = 0
# while a > 0:
#     digit = a % 10
#     reverse = reverse * 10 + digit
#     a //= 10    
# print("Reversed number:", reverse)

