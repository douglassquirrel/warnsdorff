import tour
import unittest

class FunctionalTest(unittest.TestCase):
    def testCompletesForAllBoardTypes(self):
        self.assertCompletesForSize(112)
        self.assertCompletesForSize(113)
        self.assertCompletesForSize(114)
        self.assertCompletesForSize(115)
        self.assertCompletesForSize(116)
        self.assertCompletesForSize(117)
        self.assertCompletesForSize(118)
        self.assertCompletesForSize(119)
        self.assertCompletesForSize(125)

    def assertCompletesForSize(self, size):
        print "Checking board of size %d" % (size,)
        self.assertEquals(size*size, tour.run(size, DropOutput()))

class DropOutput:
    def __init__(self):
        pass
    def write(self, data):
        pass

if __name__ == '__main__':
    unittest.main()
