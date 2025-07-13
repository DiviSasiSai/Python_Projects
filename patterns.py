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