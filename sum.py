sum=0
for i in range(1,20):
    if i%2==0 or  i%3==0 or i%4==0:
        print(end="")
    else:
        print(i)
        sum=sum+i
print("sum=",sum)
