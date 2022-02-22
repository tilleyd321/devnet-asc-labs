import unittest

def add(x,y):
    return x + y


class SimpleTest(unittest.TestCase):
    def testadd1(self):
        self.assertEqual(add(4,5),9);
    def testadd2(self):
        self.assertEqual(add(4,5),10);
    def testadd3(self):
        self.assertEqual(add(-1,-5),-6);


if __name__ == '__main__':
    unittest.main()
