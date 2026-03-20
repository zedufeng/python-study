a=int(input('first number'))
b=int(input('second number'))
c=int(input('third number'))
if(a>b)and(a>c):
    answer=a
elif(b>a)and(b>c):
    answer=b
else:
    answer=c
print(answer)#