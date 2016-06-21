'''
Write a function that takes an integer n and returns the nth iteration of
the fractal known as Sierpinski's Gasket. Here are the first few iterations.
The fractal is composed entirely of L and white-space characters; each
character has one space between it and the next (or a newline).

0
L

1
L
L L

2
L
L L
L   L
L L L L

3
L
L L
L   L
L L L L
L       L
L L     L L
L   L   L   L
L L L L L L L L
'''

def sierpinski(n):
    if n==0:
        return "L"
    print(sierpinski(n-1)+"\n"+sierpinski(n-1)+" "+sierpinski(n-1))


sierpinski(1)
sierpinski(2)