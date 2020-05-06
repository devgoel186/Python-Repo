try:
    n=int(input("No. of elements?\n"))
except:
    print("Invalid Input")
    quit()
a=list()
i=0
while i<n:
    try:
        a.append(int(input("Array element " + str(i) + "\n")))
    except:
        print("Invalid Input. Please enter an integer only")
        continue
    i+=1
i=0
while i<len(a):
    j=n-1
    while j>i:
        if a[j-1]>a[j]:
            temp=a[j]
            a[j]=a[j-1]
            a[j-1]=temp
        j-=1
    i+=1
print("Your sorted array:-\n[", end="")
for i in range(n):
    if i==n-1:
        print(a[i], end="]")
    else:
        print(a[i], end=",")
