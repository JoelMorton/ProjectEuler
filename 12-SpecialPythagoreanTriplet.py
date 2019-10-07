import math

for x in range(100):
    for y in range(100):
        a = x*x - y*y
        b = 2*x*y
        c = x*x + y*y
        root = math.sqrt(a*a + b*b)
        if root == c and a+b+c == 1000:
            print('a= ',a, 'b= ',b,'c= ', c,)
            print('product= ', a*b*c)
            print('x= ', x, 'y= ', y)
            print()

