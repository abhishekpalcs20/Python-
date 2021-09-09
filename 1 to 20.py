n=int(input("enter the number 1 to 20 which are not divisible by 2,3,5"))
for i in range(1,20):
    if i%2==0 or i%3==0 or i%5==0:
        print(" ")
    else:
            print(i)
            
            
