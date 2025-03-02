t=int(input())
b=int(input())
count=0
while count>b:
    symbol=(input())
    if symbol=="-":
        charge=(input())
        t=t-charge
        count+=count
    elif symbol=="+":
        charge=(input())
        t=t+charge
        count+=count
print(t)



    