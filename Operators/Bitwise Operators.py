a = 60 # 60 = 0011 1100

b = 13 # 13 = 0000 1101

C = 0

c = a & b; # 12 = 0000 1100

print ("Value of c is ", c)

c = a | b; # 61 = 0011 1101

print ("Value of c is ", c)

c = a^b; # 49 = 0011 0001

print ("Value of c is ", c)

C = ~a; #-61 = 1100 0011

print ("Value of c is ", c)

c = a << 2; # 240 = 1111 0000

print ("Value of c is ", c)

c = a >> 2; # 15 = 0000 1111

print ("Value of c is ", c)