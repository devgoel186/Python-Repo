name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
timedict=dict()
tmp=list()
for line in handle:
    if line.startswith("From "):
        words=line.split()
        time_word=words[5]
        hms=time_word.split(':')
        hour=hms[0]
        timedict[hour]=timedict.get(hour,0)+1
for (k,v) in timedict.items(): tmp.append((k,v))
tmp=sorted(tmp)
for (v,k) in tmp:
    print(v, k)
