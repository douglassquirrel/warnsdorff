import tour
import unittest

class TestGenerator(unittest.TestCase):
    def testWriteAndMove(self):
        out = MockFile()
        knight = MockKnight(moves = 3)
        generator = tour.Generator(knight = knight)
        generator.run(out = out)
        self.assertEquals("tour=[3,2,1,]", out.s)

class MockFile:
    def __init__(self):
        self.s = ""
    def write(self, data):
        self.s += data

class MockKnight:
    def __init__(self, moves):
        self.moves_left = moves
    def write_current_data(self, out):
        out.write(str(self.moves_left))
    def move(self):
        self.moves_left -= 1
        return (self.moves_left > 0)

if __name__ == '__main__':
    unittest.main()
