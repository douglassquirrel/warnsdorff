import tour
import unittest

class GeneratorTest(unittest.TestCase):
    def testMarksInitialLocationVisited(self):
        knight = MockKnight(moves = 3)
        generator = tour.Generator(knight = knight)
        self.assertTrue(knight.location.visited)

    def testWriteAndMove(self):
        out = MockFile()
        knight = MockKnight(moves = 3)
        generator = tour.Generator(knight = knight)
        generator.run(out = out)
        self.assertEquals("3\n2\n1\n", out.s)

class MockFile:
    def __init__(self):
        self.s = ""
    def write(self, data):
        self.s += data

class MockKnight:
    def __init__(self, moves):
        self.moves_left = moves
        self.location = MockSquare()
    def write_current_data(self, out):
        out.write(str(self.moves_left))
    def move(self):
        self.moves_left -= 1
        return (self.moves_left > 0)

class MockSquare:
    def __init__(self):
        self.visited = False

if __name__ == '__main__':
    unittest.main()
