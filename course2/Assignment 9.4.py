name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count=dict()
words=list()
for line in handle:
    if line.startswith("From "):
        words=line.split()
        count[words[1]]=count.get(words[1],0)+1
bigword=None
bigcount=None
for key in count:
    if bigcount is None or count[key]>bigcount:
        bigcount=count[key]
        bigword=key
print(bigword, bigcount)
    
