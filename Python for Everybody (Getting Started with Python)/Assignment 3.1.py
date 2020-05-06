hrs = input("Enter Hours:")
rate = input("Enter Rate:")
if(hrs<=40.0):
	print(float(hrs)*float(rate))
else:
    print(40.0*float(rate)+float(rate)*((float(hrs)-40.0)*1.5))
