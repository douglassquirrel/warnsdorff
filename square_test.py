import tour
import unittest

class SquareTest(unittest.TestCase):
    def setUp(self):
        self.board = MockBoard()
        self.square12 = tour.Square(board = self.board, x = 1, y = 2)
        self.square24 = tour.Square(board = self.board, x = 2, y = 4)
        self.square13 = tour.Square(board = self.board, x = 1, y = 3)
        self.square32 = tour.Square(board = self.board, x = 3, y = 2)
        self.board.map = {self.square12 : [],
                          self.square24 : [{"direction":1, "square":self.square13}],
                          self.square13 : [{"direction":5, "square":self.square24}],
                          self.square32 : [{"direction":2, "square":self.square13}, {"direction":4, "square":self.square24}]}
    
    def testSerialise(self):
        self.assertEquals("(1,2)", self.square12.serialise())
        self.assertEquals("(2,4)", self.square24.serialise())

    def testEquals(self):
        self.assertTrue( self.square12.equals(self.square12))
        self.assertFalse(self.square12.equals(self.square24))
        self.assertFalse(self.square12.equals(self.square13))
        self.assertFalse(self.square12.equals(self.square32))

    def testIsUnvisitedByDefault(self):
        self.assertFalse(self.square12.visited)

    def testReportsDegree(self):
        self.assertEquals(0, self.square12.degree())
        self.assertEquals(1, self.square24.degree())
        self.assertEquals(1, self.square13.degree())
        self.assertEquals(2, self.square32.degree())

    def testReportsNoNeighbours(self):
        self.assertTrue( self.square12.has_no_neighbours())
        self.assertFalse(self.square24.has_no_neighbours())
        self.assertFalse(self.square13.has_no_neighbours())
        self.assertFalse(self.square32.has_no_neighbours())
        
    def testPicksNeighbourWithoutTiebreak(self):
        choice = self.square32.pick_neighbour(lambda x : x["direction"], None)
        self.assertEquals((self.square13, False), choice)
        choice = self.square32.pick_neighbour(lambda x : -x["direction"], None)
        self.assertEquals((self.square24, False), choice)

    def testPicksNeighbourWithTiebreak(self):
        choice = self.square32.pick_neighbour(lambda x : x["square"].degree(), lambda x : x["direction"])
        self.assertEquals((self.square13, True), choice)
        choice = self.square32.pick_neighbour(lambda x : x["square"].degree(), lambda x : -x["direction"])
        self.assertEquals((self.square24, True), choice)

class MockBoard:
    def __init__(self):
        pass
    def get_unvisited_neighbours(self, square):
        return self.map[square]

if __name__ == '__main__':
    unittest.main()
