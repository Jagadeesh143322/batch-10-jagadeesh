# ----> while loop
# ------> break using while loop

# Eg:1
# 1.) Iterate from 20 to 30 and break the loop in 27

# 1.)

i = 20
while i<31:
    if i ==27:
        break
    print(i)
    i+=1

# 2.)

i = 20
while i<31:
    print(i)
    i+=1
    if i ==27:
        break
    i+=1
    
# 3.)

i = 20
while i<31:
      print(i)
      if i ==27:
         break
      i+=1

# ! ------> continue
#  ----> Eg:1
i = 20
while i<31:
    if i==29:
        continue
    print(i)
    i=i+1

i = 20
while i<31:
    i=i+1
    if i ==27:
        continue
    print(i)

# ! Eg:5
# while to iterate from 12 to 22
# find the sum of all numbers

# i = 12
# sum=0
# while i<23:
#     sum=sum+i
#     i+=1
#  print(sum)
'''
i = 12
add=0
while i<=23:
    add+=i
    i+=1
    if i==23:
        print("sum of number is:",add)

# Eg:6
# find the avarage of value from 20 to 30

i = 20
sum = 0
count = 0
while i<=30:
    sum = sum+i
    i+=1
print(sum/count)




    

'''
# ----> while loop
# ------> break using while loop

# Eg:1
# 1.) Iterate from 20 to 30 and break the loop in 27

# 1.)

i = 20
while i<31:
    if i ==27:
        break
    print(i)
    i+=1

# 2.)

i = 20
while i<31:
    print(i)
    i+=1
    if i ==27:
        break
    i+=1
    
# 3.)

i = 20
while i<31:
      print(i)
      if i ==27:
         break
      i+=1

# ! ------> continue
#  ----> Eg:1
i = 20
while i<31:
    if i==29:
        continue
    print(i)
    i=i+1

i = 20
while i<31:
    i=i+1
    if i ==27:
        continue
    print(i)

# ! Eg:5
# while to iterate from 12 to 22
# find the sum of all numbers

# i = 12
# sum=0
# while i<23:
#     sum=sum+i
#     i+=1
#  print(s0000
i = 12
add=0
while i<=23:
    add+=i
    i+=1

    if i==23:
        print("sum of number is:",add)

# Eg:6
# find the avarage of value from 20 to 30

i = 20
sum = 0
count = 0
while i<=30:
    sum = sum+i
    i+=1
print(sum/count)
                # ------> nested for loop
# eg:1
# for row in range (1, 3+1):
#     for col in range (1, 4+1):
#        print(row,col)

# eg:2
# * * * *
# * * * *
# * * * *
# * * * *

row = int(input("enter the rows: "))
col = int(input("enter the cols: "))

# for row in range (rows):
#     for col in range (cols):
#        print("*",end=" ")
#     print()

# sum = 0
# for now in ranges(5):
#     for col in range(5):
#         sum = sum + 1
#       print(sum, end=" ")
#     print()


# ! to print stars in right angled triangle
# for row in range (0, 6):
#    for col in range(0, row+1):
#        print("*",end=" ")
#    print()

# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# for row in range (0, 6):
#    for col in range (0, row):
#        print("*", end=" ")0000000000000000000 
#       print()

# * * * * *
# *       *
# *       *
# *       *
# * * * * *

# for row in range (5):
#    for col in range (5):
#        if col==0 or col==5-1 or row==0 or row==5-1
#       print("*",end=" ")
#        else:
#       print("*", end=" ")
#     print()

#       *
#     * * *
#    * * * *
#   * * * * *

# for row in range (0, 5):
#     for col in range (0, 6):
#         if ((row==0 and col==3) or ( row==1 and ( col>=2 and col<=4) or ( row==2 and. ( col>=1 and col<=5))))

#       print ("*", end=" ")
#       else:
#       print (" ", end=")
#     print()


# *
# * *
# *   *
# *     *
# *       *
# * * * * * *






  
    
    
s1 = "hello world to all"                                        
