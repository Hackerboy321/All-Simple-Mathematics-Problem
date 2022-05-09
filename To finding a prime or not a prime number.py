L= []
num = int(input("enter any number"))
for i in range(1,num+1):
    if num%i==0:
     L.append(i)
     D=len(L)
if D==2:
 print("This",num," is Prime number")
if D > 2 :
    print("This",num," is not Prime number")
