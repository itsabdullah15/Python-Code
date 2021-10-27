# no. of n digit which are equall to sum of nth power of its digits
# 153 = 1^3 + 5^3 + 3^3 = 3+125+27 = 153 Armstrong number
# 153/10 = 3 

# for i in range(1001):
#     num=i
#     result=0
#     n=len(str(i))
#     while(i!=0):
#         digit=i%10
#         result=result+digit**n
#         i=i//10
#     if num==result:
#         print(num)

# print(153//10)

for i in range(1001):
    num=i
    result=0
    n=len(str(i))
    while(i!=0):
        digit=i%10
        result=result+digit**n
        i=i//10
    if num==result:
        print(result)    

