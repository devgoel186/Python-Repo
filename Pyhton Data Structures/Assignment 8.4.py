fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    lst+=line.split()
lst2=list()
for word in lst:
    if word not in lst2:
        lst2.append(word)
lst2.sort()
print(lst2)
