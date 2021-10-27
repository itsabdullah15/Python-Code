# 1
# 1 2
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# n = int(input("Enter the number of row: "))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print() 

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# 1 
# 22
# 333
# 4444
# 55555

# n=int(input("Enter the number of row: "))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# *
# **
# * *
# *  *
# *****

# n = int(input("Enter the number of rows: "))
# for row in range(n):
#     for col in range(n):
#         if col==0 or row==(n-1) or row==col:
#             print("*",end="")
#         else:
#             print(end=" ")
#     print() 

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# 1 2 3 4 5 
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9
# num = int(input("Enter the number of rows: "))
# n_list = [[0 for x in range(num)] for y in range(num)]
# n=1
# low=0
# high=num-1
# count = int((num+1/2))
# for i in range(count):
#     for j in range(low,high+1):
#         n_list[i][j]=n
#         n=n+1
#     for j in range(low+1,high+1):
#         n_list[j][high]=n
#         n=n+1
#     for j in range(high-1,low-1,-1):
#         n_list[high][j]=n
#         n=n+1
#     for j in range(high-1,low,-1):
#         n_list[j][low]=n
#         n=n+1
#     low=low+1
#     high=high-1


# for i in range(num):
#     for j in range(num):
#         print(n_list[i][j],end="\t")
#     print()

# num=int(input("Enter thr number of rows: "))
# n_list=[[0 for x in range(num)] for y in range(num)]
# n=1
# low=0
# high=num-1
# count = int((num+1)/2)
# for i in range(count):
#     for j in range(low,high+1):
#         n_list[i][j]=n
#         n=n+1
#     for j in range(low+1,high+1):
#         n_list[j][high]=n
#         n=n+1
#     for j in range(high-1,low-1,-1):
#         n_list[high][j]=n
#         n=n+1
#     for j in range(high-1,low,-1):
#         n_list[j][low]=n    
#         n=n+1
#     low=low+1
#     high=high-1    

# for i in range(num):
#     for j in range(num):
#         print(n_list[i][j],end='\t')
#     print()    

# print(n_list)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#  ** **
# *  *  *
# *     *
#  *   *
#   * *
#    *

for row in range(6):
    for col in range(7):
        if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
            print("*",end="")
        else:
            print(end=" ")
    print()             