hrs = input("Enter Hours:")
h = float(hrs)
rate=float(input("enter rate"))
if(h<40):
    money=h*rate
else:
    h=1.5*(h- 40)+h
    money=h*rate
print(money)