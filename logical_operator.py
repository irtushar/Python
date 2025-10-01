'''
Logical Operators - Working with Boolean Values
and
or
not
'''

print(10 - 4 == 6 and 10-5 == 15)
print(10 - 4 == 6 and 10-5 == 5)

print(10 - 4 == 6 or 10 - 5 == 15)
print(10 - 4 == 6 or 10 - 5 == 5)

print(not(10 - 4 == 6))

marks = 85
if marks >= 80 and marks <= 100:
    print("A+")
elif marks >= 70 and marks < 80:
    print("A")
elif marks >= 60 and marks < 70:
    print("A-")
elif marks >= 50 and marks < 60:
    print("B")
else:
    print("Fail")    
    

