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
    min=i
    j=i+1
    while j<n:
        if a[j]<a[min]:
            min=j
        j+=1
    temp=a[i]
    a[i]=a[min]
    a[min]=temp
    i+=1
print("[", end="")
for i in range(n):
    if i==n-1:
        print(a[i], end="]")
    else:
        print(a[i], end=",")
