a=int(input("Enter the number:"))
b=input("Enter 1 or 0 :")
if b=="1":
    for i in range(0,a+1):
        print("*"*i)
        continue
if b=="0":
    for i in range(a,0,-1):
        print("*"*i)
        continue