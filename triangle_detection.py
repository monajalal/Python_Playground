'''
Implement a method that accepts 3 integer values a, b, c. The method should return
true if a triangle can be built with the sides of given length and false in any
other case. (In this case, all triangles must have surface greater than 0 to be accepted).
'''

def is_triangle(a, b, c):
    for side in [a, b, c]:
        if side <= 0:
            return False
    sides = [ [a, b, c], [b, a, c], [c, a, b]]
    for side in sides:
        if side[0] + side[1] < side[2]:
            return False
        if abs(side[0] - side[1]) >= side[2]:
            return False
    return True

print(is_triangle(7, 2, 2))
print(is_triangle(4, 2, 3))
print(is_triangle(1, 2, 3))


