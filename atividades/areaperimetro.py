a = float(input('Digite '))
b = float(input('Digite '))
c = float(input('Digite '))
if (a + b < c) or (a + c < b) or (b + c < a):
    print('Perimetro é = {} '.format(a+b+c))
else:
    print('Area é = {} '.format((a+b) * c / 2))

