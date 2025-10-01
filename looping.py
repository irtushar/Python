'''
Type of loop in Python
for loop
while loop
nested loop
'''
#range function
# for loop

# for i in range(10):
#     print(i)

# a = list(range(10))
# print(a)

# range (start, stop, step)
# b = list(range(10))
# c = list(range(0, 10))
# d = list(range(2, 5))
# e = list(range(1, 10, 2))
# print(b)
# print(c) 
# print(d)
# print(e)


# y = list(range(10, 0, -1)) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(y)

# a =  "Hello World"
# for letter in a:
#     print(letter)

# shoping = ["mango", "banana", "apple",3, 5.6, -33, 70,5]
# for item in shoping:
#     print(item)

# list = [2, 3, 4, 5, 6, 7, 8, 9, 50, 70, 80, 40, 60, 90] 
# for i in list:
#     if i <= 10:
#         print(i)
    
# for i in range(20):
#        if i % 3 == 0 and i % 5 == 0:
#            print(f"{i} is divisible by 3 and 5")

# sum = 0
# for i in range(1, 10):
#     sum = sum + i
# print(sum)



# while loop

# a = 0
# while a < 10:
#     a += 1
#     print(a)

#break

# for i in range(10):
#     if i == 5:
#         break
#     print(i)   

# a = 1
# while a <= 10:
#     a = a + 1
#     if a == 5:
#         break
#     print(a)

#continue

# for i in range(10):
#     if i == 5:
#         continue
#     print(i)

# a = 1
# while a <= 10:
#     a = a + 1
#     if a == 5:
#         continue
#     print(a)    

#infinite loop

# for i in range(10,):
#     print(i)

# a = 10
# while a >= 0:
#     a = a - 1
#     print(a)

# while True:
#     a = input("Enter a name: ")
#     print("Hello", a, "Good Morning")


# while True:
#     a = input("Enter a name: ")
#     if a == "exit" or a == "q":
#         break
#     print("Hello", a, "Good Morning")

#nested loop
# for i in range(1,6):
#     for j in range(1,6):
#         print(i*j, end=" ")
#     print()

#Print a pattern
# for i in range(7):
#     for j in range(i+1):
#         print("#", end=" ")
#     print()    

# for i in range(7):
#     for j in range(i+1):
#         print(chr(97+i), end=" ")
#     print()      

'''
nested list
traverse
'''

# shopping_list = [["apple","mango"], ["banana","pineapple"], ["orange","grapes"],[12,15,18],["pizza",2.5,80]]

# for item in shopping_list:
#     # print(item)
#     for sub_item in item:
#         print(sub_item)