# part - 1

# example - 1
# iteration with list comprehension

# a = [10,20,40,50,60]
# b = [i+5 for i in a]
# print(b)

# example - 2
# iterating through a string using list comprehension

# a = "Hello World!"
# # b = [ i for i in a]
# #or
# b = list(a)
# print (b)


# example - 3
# using range() function in list comprehension

# a = [i for i in range(1, 20, 2)]
# print(a)
# b = [i for i in range(2, 20, 2)]
# print(b)

# part - 2

# example - 4
# using if with list 

# a = []
# for i in range (1, 20):
#     if i%3 == 0:
#         a.append(i)
# print(a)       

# or
# a = [i for i in range(1, 20) if i%3 == 0] 
# print(a)

# example - 5
# nested if with list

# a = []
# for i in range (1, 20):
#     if i%3 == 0:
#         a.append(i)
#     if i%5 == 0:    
#         a.append(i)
# print(a)     

# or
# a = [i for i in range(1, 20) if i%3 == 0 or i%5 == 0] 
# print(a)

# example - 6
# if....else with list 

# a = []
# for i in range(20):
#     if i % 2 == 0:
#         a.append("Even")
#     else:
#         a.append("Odd")   
# print(a) 

# or
# a = ["Even" if i%2 == 0 else "Odd" for i in range(20)]
# print(a)
