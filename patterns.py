# Patern 1
#        1
#       212
#      32123
#     4321234
#    543212345
#   65432123456
#  7654321234567
#
#
# n=7
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(i+1,0,-1):
#         print(k,end="")
#     for k in range(2,i+2):
#         print(k,end="")
#     print()

# #Square Pattern
# *****
# *****
# *****
# *****
# *****
# n=5
# for i in range(n):
#     for j in range(n):
#         print("*",end="")
#     print()

# Pattern Right Triangle
# *
# **
# ***
# ****
# *****
# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end="")
#     print()

# #Pattern Left Triangle
#     *
#    **
#   ***
#  ****
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(i+1):
#         print("*",end="")
#     print()

# #Pyramid
#      *
#     ***
#    *****
#   *******
#  *********
# n=5
# for i in range(n):
#     for j in range(n - i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end="")
#     for l in range(i+1):
#         print("*",end="")
#     print()

#Diamond
#      *
#     ***
#    *****
#   *******
#  *********
#   *******
#    *****
#     ***
#      *
#
# n=5
# for i in range(n):
#     for j in range(n - i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end="")
#     for l in range(i+1):
#         print("*",end="")
#     print()
# for i in range(n-1):
#     for j in range(i+2):
#         print(" ",end="")
#     for k in range(n-i-2):
#         print("*",end="")
#     for l in range(n-i-1):
#         print("*",end="")
#     print()

#Hollow Square
# *****
# *   *
# *   *
# *   *
# *****
# n=5
# for i in range(n):
#     if i==0 or i==n-1:
#         for k in range(n):
#             print("*",end="")
#         print()
#     else:
#         print("*",end="")
#         for i in range(n-2):
#             print(" ",end="")
#         print("*",end="")
#         print()

#Number Pattern
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
#
# n=5
# num=1
# for i in range(n):
#     for j in range(i+1):
#         print(num,end=" ")
#         num+=1
#     print()
#

#Alphabet Pattern
# A
# B C
# D E F
# G H I J
# K L M N O
#
# n=5
# num='A'
# for i in range(n):
#     for j in range(i+1):
#         print(chr(ord(num)),end=" ")
#         num=chr(ord(num)+1)
#     print()

#pasclas Triangle Patter
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    num = 1
    for k in range(i+1):
        print(num,end=" ")
        num = num*(i-k)//(k+1)
    print()