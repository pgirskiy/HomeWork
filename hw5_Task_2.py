import unittest


# Функции из домашнего задания


def is_year_leap(year):
    '''
    :param year: year
    :return: True or False
    '''
    if isinstance(year, int) and year > 1:
        if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False


def is_triangle(a, b, c):
    '''
    :param a: side a
    :param b: side b
    :param c: side c
    :return: True or False
    '''
    if (a + b) > c and (b + c) > a and (a + c) > b:
        return True
    else:
        return False


def full_triangle_info(a, b, c):
    '''
    :param a: side a
    :param b: side b
    :param c: side c
    :return: txt string
    '''
    if (a + b) > c and (b + c) > a and (a + c) > b:
        if a == b == c:
            return 'равносторонний'
        elif a == b or a == c or b == c:
            return 'равнобедренный'
        else:
            return 'разносторонний'
    else:
        return None


class TestYear(unittest.TestCase):

    def testMinusValue(self):
        self.assertFalse(is_year_leap(-1))

    def testAssertTrue(self):
        self.assertTrue(is_year_leap(2016))

    def testAssertFalse(self):
        self.assertFalse(is_year_leap(2010))

    def testTypeErr(self):
        self.assertRaises(TypeError, is_year_leap, "a")

    def testZeroPoint1(self):
        self.assertIsNone(is_year_leap(0))


class TestIsTriangle(unittest.TestCase):


    def testMinusValue(self):
        self.assertFalse(is_triangle(-1, -1, -1))

    def testAssertTrue(self):
        self.assertTrue(is_triangle(2, 2, 2))

    def testAssertFalse(self):
        triang = ((1, 1, 1), (1, 4, 4), (6, 9, 12), (3, 9, 9))
        for el in triang:
            self.assertTrue(is_triangle(el[0], el[1], el[2]))

    def testTypeErr(self):
        self.assertRaises(TypeError, is_triangle, "a", "b", "c123")

    def testNoArg(self):
        self.assertRaises(TypeError, is_triangle)


class TestFullTriangleInfo(unittest.TestCase):
    def testMinusValue(self):
        self.assertFalse(full_triangle_info(-5, -5, -2))

    def testNoneReturn(self):
        self.assertIsNone(full_triangle_info(44, -10, 11))

    def testAssertEqual3(self):
        self.assertNotEqual(is_triangle(2, 2, 2), "равносторонний")

    def testAssertEqual4(self):
        self.assertNotEqual(is_triangle(2, 2, 4), "равнобедренный")

unittest.main()

