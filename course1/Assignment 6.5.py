text = "X-DSPAM-Confidence:    0.8475";
length=len(text)
c=1
while True:
    c=c+1
    pos=text.find(' ')
    if(c==length):
        break
print(float(text[pos:]))
