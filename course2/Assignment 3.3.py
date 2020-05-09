score = input("Enter Score (between 0.0 and 1.0) : ")
scr=float(score)
if(scr>=0.0 and scr<=1.0):
	if(scr>=0.9):
		print("A")
	elif(scr>=0.8):
    	print('B')
	elif(scr>=0.7):
    	print('C')
	elif(scr>=0.6):
		print('D')
else:
	print("F")


    
