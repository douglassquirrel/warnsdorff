import tour
import unittest

class BoardTest(unittest.TestCase):
    def testGetsSquaresByRowAndColumn(self):
        board = tour.Board(10)
        self.assertTrue(tour.Square(board=board, x=1, y=1).equals(board.get_square_at(x=1, y=1)))
        self.assertTrue(tour.Square(board=board, x=7, y=1).equals(board.get_square_at(x=7, y=1)))
        self.assertTrue(tour.Square(board=board, x=10, y=1).equals(board.get_square_at(x=10, y=1)))
        self.assertTrue(tour.Square(board=board, x=10, y=10).equals(board.get_square_at(x=10, y=10)))
    def testReturnsNoneForInvalidSquare(self):
        board = tour.Board(10)
        self.assertEquals(None, board.get_square_at(x=-1, y=1 ))
        self.assertEquals(None, board.get_square_at(x=1,  y=-1))
        self.assertEquals(None, board.get_square_at(x=11, y=1 ))
        self.assertEquals(None, board.get_square_at(x=5,  y=11))
        self.assertEquals(None, board.get_square_at(x=11, y=11))
        self.assertEquals(None, board.get_square_at(x=99, y=99))
        self.assertEquals(None, board.get_square_at(x=-9, y=99))
    def testReturnsUnvisitedNeighbours(self):
        board = tour.Board(10)
        self.assertEquals([{"direction":3, "square":board.get_square_at(x=2, y=3)}, \
                           {"direction":4, "square":board.get_square_at(x=3, y=2)}],
                          board.get_unvisited_neighbours(board.get_square_at(x=1, y=1)))
        self.assertEquals([{"direction":1, "square":board.get_square_at(x=2, y=5)}, \
                           {"direction":2, "square":board.get_square_at(x=3, y=6)}, \
                           {"direction":3, "square":board.get_square_at(x=5, y=6)}, \
                           {"direction":4, "square":board.get_square_at(x=6, y=5)}, \
                           {"direction":5, "square":board.get_square_at(x=6, y=3)}, \
                           {"direction":6, "square":board.get_square_at(x=5, y=2)}, \
                           {"direction":7, "square":board.get_square_at(x=3, y=2)}, \
                           {"direction":8, "square":board.get_square_at(x=2, y=3)}], \
                          board.get_unvisited_neighbours(board.get_square_at(x=4, y=4)))

        board.get_square_at(x=3, y=2).visited = True
        self.assertEquals([{"direction":3, "square":board.get_square_at(x=2, y=3)}], \
                          board.get_unvisited_neighbours(board.get_square_at(x=1, y=1)))
        self.assertEquals([{"direction":1, "square":board.get_square_at(x=2, y=5)}, \
                           {"direction":2, "square":board.get_square_at(x=3, y=6)}, \
                           {"direction":3, "square":board.get_square_at(x=5, y=6)}, \
                           {"direction":4, "square":board.get_square_at(x=6, y=5)}, \
                           {"direction":5, "square":board.get_square_at(x=6, y=3)}, \
                           {"direction":6, "square":board.get_square_at(x=5, y=2)}, \
                           {"direction":8, "square":board.get_square_at(x=2, y=3)}], \
                          board.get_unvisited_neighbours(board.get_square_at(x=4, y=4)))

if __name__ == '__main__':
    unittest.main()
