import unittest

def class_triangle(a:int, b:int, c:int):
    """This function classify the triangle that you input"""
    # equilateral triangles have all three sides with the same length
    if a == b == c:
        return "This triangle is a equilateral triangle"
    # it is not a triangle if one side is bigger than the sum of two other sides
    elif a >= b+c or b >= a+c or c >= a+b:
        return "The length you input is not a triangle"
    # isosceles triangles have two sides with the same length
    elif a == b or b == c or a == c:
        return "This triangle is a isosceles triangle"
    # right triangles have three sides with lengths, a, b, and c where a2 + b2 = c2
    elif (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == a**2 + b**2):
        return "This triangle is a right triangle"
    # scalene triangles have three sides with different lengths
    else:
        return "This triangle is a normal triangle which is scalene"

def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('class_triangle(',a, ',', b, ',', c, '): ',class_triangle(a,b,c),sep="")

class TestTriangles(unittest.TestCase):
    def test_Set1(self): # test not triangles
        self.assertEqual(class_triangle(4,2,2),"The length you input is not a triangle")
        self.assertEqual(class_triangle(2,2,10),"The length you input is not a triangle")
        self.assertEqual(class_triangle(2,5,1),"The length you input is not a triangle")
    def test_Set2(self): # test equlateral triangles
        self.assertEqual(class_triangle(1,1,1),"This triangle is a equilateral triangle")
        self.assertEqual(class_triangle(7,7,7),"This triangle is a equilateral triangle")
        self.assertEqual(class_triangle(10,10,10),"This triangle is a equilateral triangle")
    def test_Set3(self): # test isosceles triangles
        self.assertEqual(class_triangle(3,3,4),"This triangle is a isosceles triangle")
        self.assertEqual(class_triangle(5,5,9),"This triangle is a isosceles triangle")
    def test_Set4(self): # test right triangles
        self.assertEqual(class_triangle(3,4,5),"This triangle is a right triangle")
        self.assertEqual(class_triangle(5,4,3),"This triangle is a right triangle")
        self.assertEqual(class_triangle(4,5,3),"This triangle is a right triangle")
        self.assertEqual(class_triangle(6,10,8),"This triangle is a right triangle")
    def test_Set5(self): # test scalene triangles
        self.assertEqual(class_triangle(3,5,7),"This triangle is a normal triangle which is scalene")
        self.assertEqual(class_triangle(10,15,23),"This triangle is a normal triangle which is scalene")
        self.assertEqual(class_triangle(100,111,145),"This triangle is a normal triangle which is scalene")

if __name__ == "__main__":
    runClassifyTriangle(1,1,1)
    runClassifyTriangle(1,5,7)
    runClassifyTriangle(10,6,8)
    runClassifyTriangle(100,111,134)
    unittest.main(argv=['first-arg-is-ignored'], exit = False)
