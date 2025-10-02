# problem - 1
# swapping two list elements

# a = [17,12,13,15,16,10]
# temp = a[0]
# a[0] = a[-1]
# a[-1] = temp
# print(a)


# problem - 2
# count unique elements in an list

# a = [1,2,2,3,3,3,3,4,5,6]
# b = []
# count = 0
# for i in a:
#     if i not in b:
#         count += 1
#         b.append(i)
# print(count)        

# problem - 3
'''
given a list, extract all elements whose frequency is grater than K.
Input: test_list = [4,6,4,3,3,4,3,4,3,8], K = 3
Output: [4,3]
'''
# test_list = [4,6,4,3,3,4,3,4,3,8]
# K = 3
# res = []
# for i in test_list:
#     freq = test_list.count(i)
#     if freq > K and i not in res:
#         res.append(i)
# print(res)        

# problem - 4
'''
create the following list using list comprehension
[[1,2,3,4],[0,1,3,4],[0,1,3,4],[0,1,2,4],[0,1,2,3]]
'''

# a = [[j for j in range(5) if i!=j] for i in range(5)]
# print(a)