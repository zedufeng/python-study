def computepay(h, r):
    if(h<=40):
        return h*r
    else:
        return (h-40)*1.5*r+40*r
rate=float(input('Enter rate'))
hrs = float(input("Enter Hours:"))
pay = computepay(hrs,rate )
print("Pay:",pay)