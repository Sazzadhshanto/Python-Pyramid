i=1
while i<10:
    print("*" * i)
    i+=1
    x =10
    for i in range(1, x+1):
        print(" "* (80-i),end="")
        print("*" * (2*i-1))
