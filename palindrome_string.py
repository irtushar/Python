'''
input: "madam"
output: "yes"
'''

a = input("Enter a string: ")
if a== a[::-1]:
    print("Yes")
else:
    print("No")    