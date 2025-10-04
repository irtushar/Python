'''
input: "I love coding using python"
output: "I evol gnidoc gnisu nohtyp"
'''


a = input("Enter a String: ").strip('"')
a = a.split()
print(a)
result = ""
for i in a:
    result += i[::-1] + " "
print(result)    
