#program to calculate discount
print('Enter price of purchases: ')
x=int(input())
if (x<1000):
    print('no discount')
    print('total bill amount',x,sep='______')
elif (1000<=x<=1999):
    print('discount is 10%')
    a=(x-(x*0.1))
    print('total bill amount',a,sep='______')
elif (2000<=x<=2999):
    print('discount is 20%')
    b=(x-(x*0.2))
    print('total bill amount',b,sep='______')
elif (3000<=x<=4999):
    print('discount is 30%')
    c=(x-(x*0.3))
    print('total bill amount',c,sep='______')
else:
    print('discount is 40%')
    d=(x-(x*0.4))
    print('total bill amount',d,sep='______')
