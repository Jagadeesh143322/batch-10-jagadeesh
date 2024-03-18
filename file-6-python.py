
n = 128
while n!=0:
    rem = n%10
    print(rem)
    n = n/10



  #s1 =input("enter string:")
  #fst =s1[0].upper()
  #1st =s1[1].upper()
 # print(fst+s1[1:1en(s1)-1]+1st)

  #print(s1.replace('h','H')
# ! -----> set
# characteristics of set
#1.)Python program to captilalize the first and last character of each word in a string
#2.)Input:128
#ouput:Yes
#128%1==0,128%2==0, and 128%8==0.
#3.)l1=[1,2,3,4],l2=[5,6,7,8]
#add both l1 and l2 and ans=[6,8,10,12]


#n = 128
#for i in n:
#    print(i)


#n = 128
#while n!=0:
#    rem = n%10
#    print(rem)
#    n = n/10

#n = 128
#for i in str(n):
#    print(i)

n = 128678
temp = n
str1 = ""
while n!= 0:
    rem = n%10
    check = temp % n
    n = n//10
n=128
if n % 1==0 and n % 2==0 and n % 8==0:
    print("yes")
else:
    print("No")
l1 = [8, 9, 0, 7]
l2 = [7, 6, 5, 4]

#print(l1[0]+l2[0], l1[1]+l2[1])
l3 = []
for val in range(len(l1)):
    ans = l1[val]+l2[val]
    l3.append(ans)
print(l3)
# Eg:1
s1 = {9, 9, 89, 7.76, 8+7j, (8, 7, 5), "truck", 'e'}
print(s1)
# Eg:1
#s1 = {9, 9, 89, 7.76, 8+7j, (8, 7, 5), "truck", 'e'}
#print(s1)

# * Eg:2
#s2 = {5, 8, 98, [9, 0]}
#print(s2) ----> error


# Eg: 4
# min(), max(), len()

# * Eg:
# ? to add element inside set

s1 = {8, 78, 67, 'u'}
#add
#s1.add(43)
print(s1)
# * Eg:2
#s2 = {5, 8, 98, [9, 0]}
#print(s2) ----> error


# Eg: 4
# min(), max(), len()

# * Eg:
# ? to add element inside set

s1 = {8, 78, 67, 'u'}
#add
#s1.add(43)
print(s1)

# min(), max(), len()

# Eg:4,
# ? to add element inside set
#s1 = {8, 78, 67, 'u'}
#add
#s1.add(43)
#print(s1)

# update()
##s1.update(9, 0)
##print(s1)

#To deleat element inside set

s1 = {8, 78, 67, 'u'}
 lklkjkljojopsij][l
                  lkj[kj\p\


                      lkda];sldkAOJD
                  ;LJASLKD\
                  ojd
                  dljA
                  'SD;'KADL;JDPOKD
                  L;;SPOJDOKQLL
                  ;LJPDOJQUKQWJ
                  QWJPO
                  WQEQW
                  E1
                  23PO4EJLKFJLEF
                  JAD
                  ;KLAFJ
                  ASFJAF
                  LA;JF
                  A'O
                  ;LF
                  JFLSKDF
                  LJF
                  ;LFKWEILKF
                  akfpe'lkm
                  p
                  j
                  ff

                  po
                  ;ad
                  dpojjl;o
                  fl;fp;f[pf[p;fl'ff
                             ff[d';l]-';;f\]
                                a'l
                                ';L
                                ;

                                ;
                                WL;
                                ]EO
                             "
#pop() # to deleat one element randomly
##s1.pop()
##print(s1)
##
##remove()
s1.remove(78)

print(s1)

#discard()
##s1.discard(67)
##print(s1)
# update()
#s1.update([9, 0])
#print(s1)


# ? To delete element inside set
s1 = {8, 78, 67, 'u'}


# pop() # ---> To delete one element randomly
#s1.pop()
#print(s1)

#  ---> remove()
#s1.remove(78)
#print(s1)

# discard()
#s1.discard(8967)
#print(s1)


# clear()
#l1 = {}
#print(type(l1)) #---> datatype is dict

#s1 = set() # to create empty set
#print(type(s1))
# ? to delete element inside set
s1 = {8, 78, 67, 'u'}


# pop() # to delete one element randonly
# s1.pop()
# print(s1)

# remove()
s1.remove(78)
print(s1)

# discard()
s1.discard(8967)
print(s1)


# clear()
l1 = {}
print(type(l1)) ---- datatype is dict

s1 = set() # to creat empty set
print(type(s1))
# clear()
'''
l1 = {}
print(type(l1)) 
'''

'''
s1 = set() # --> to create empty set
print(type(s1))
'''

'''
s1 = {8,9,0}
s1.clear()
print(s1)
'''

'''
s1 = {8,9,0}
del s1
print(s1)
'''
# join the sets
# union() --> to combine 2 sets
'''
s1 = {9,0,8}
s2 = {9.90,"caed",'t',56}
s3 = s1.union(s2)
print(s3)
'''
# intersection() --> to get common elements inside set
'''
s1 = {4,5,6}
s2 = {5,6,7,8}
print(s1.intersection(s2))
'''
# difference{}
s1 = {4,5,6}
s2 = {5,6,7,8}
print(s1.difference(s2))
print(s2.difference(s1))
# isdisjoit(), issubset(), issuperset()

#s1 = {8, 9, 0}
#s2 = {6, 7, 5, 8, 9, 0}

#print(s1.issubset(s2))
#print(s2.issuperset(s1))
s1 = {1,2,3,4,5}
s2 = {3,2,7,8,9}

for val in s1:
    if val in s2:
        str1 = "Its joint set"
print(str1)
# intersection() ---> to get common elements inside set
s1 = {4, 5, 6}
s2 = {5, 6, 7, 8, 9}
print(s1.intersection(s2))

# n1 = {1,2,3} --> s1

for val in s1:
    if val in s2:
        str1 = "its joint set"

