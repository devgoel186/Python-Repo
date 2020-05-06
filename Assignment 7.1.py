# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
string = ((fh.read()).upper()).rstrip()
print(string)
