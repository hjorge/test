import math as m

#Initialization
B= 67 * 7919

j= B+1
i=1
C1=2*j-1
C2=1

#Auxiliary function to calculate gcd
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

#Algorithm
while((C1-C2)!= 0):
   while(C1 > C2):
     i+=1
     C2 += 2*i-1
     print "i = ", i
   if (C1 < C2):
      j += 1
      C1 += 2*j -1
      print "j = ", j

#Results of the calculation
A = j
C = i
GDC = gcd (A,C)

#Printing the Results
print "Valor de C: ", C
print "Valor de A: ", A

if (GDC == 1):
   print "O triangulo encontrado era primitivo"
   print "Valor de m: ", int(m.sqrt(A+C))
   print "Valor de n: ", int(m.sqrt(A-C))
else:
   print "O triangulo encontrado NAO era primitivo"
   print "Valor de m: ", GDC
   print "Valor de n: ", B/GDC
