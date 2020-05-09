def computepay(h,r):
    hrs1=float(hrs)
    rate1=float(rate)
    if hrs1<=40:
        pay=hrs1*rate1
    else:
        pay=40*rate1+(hrs1-40)*rate1*1.5
    return pay
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
p = computepay(10,20)
print("Pay",p)
