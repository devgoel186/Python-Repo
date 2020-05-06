# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
s=0.0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        pos=line.find(':')
        line1=line[pos+1:]
        line1=line1.strip()
        s=s+(float(line1))
        count+=1
print("Average spam confidence:", s/count)
