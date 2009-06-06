import tour
import unittest

class KnightTest(unittest.TestCase):
    def setUp(self):
        self.square21 = MockSquare(x = 2, y = 1, has_nbrs = True)
        self.rule = MockRule(new_location = self.square21, tiebreak = False)        

    def testWritesCurrentData(self):
        location = MockSquare(x = 0, y = 0, has_nbrs = True)
        out = MockFile()

        knight = tour.Knight(location = location, initial_rule = self.rule)
        knight.write_current_data(out)

        self.assertEquals("{'square':(0,0), 'tiebreak':False}", out.s)

        location = MockSquare(x = 1, y = 1, has_nbrs = True)
        out = MockFile()

        knight = tour.Knight(location = location, initial_rule = self.rule)
        knight.write_current_data(out)

        self.assertEquals("{'square':(1,1), 'tiebreak':False}", out.s)

    def testMoveReturnsFalseIfDone(self):
        location = MockSquare(x = 0, y = 0, has_nbrs = False)
        knight = tour.Knight(location = location, initial_rule = self.rule)
        self.assertFalse(knight.move())

    def testMovesWhenPossible(self):
        location = MockSquare(x = 0, y = 0, has_nbrs = True)
        knight = tour.Knight(location = location, initial_rule = self.rule)
        self.assertTrue(knight.move())

    def testMoveMarksSquareVisited(self):
        location = MockSquare(x = 0, y = 0, has_nbrs = True)
        knight = tour.Knight(location = location, initial_rule = self.rule)
        knight.move()
        self.assertTrue(self.square21.visited)
        
    def testMoveInvokesRuleOnCurrentSquare(self):
        location = MockSquare(x = 0, y = 0, has_nbrs = True)
        out = MockFile()

        knight = tour.Knight(location = location, initial_rule = self.rule)
        knight.move()
        knight.write_current_data(out)

        self.assertEquals(location, self.rule.invoked_on) 
        
    def testMoveUpdatesLocation(self):
        location = MockSquare(x = 0, y = 0, has_nbrs = True)
        out = MockFile()

        knight = tour.Knight(location = location, initial_rule = self.rule)
        knight.move()
        knight.write_current_data(out)

        self.assertEquals("{'square':(2,1), 'tiebreak':False}", out.s)  
        
    def testMoveUpdatesRule(self):
        location = MockSquare(x = 0, y = 0, has_nbrs = True)
        self.square40 = MockSquare(x = 4, y = 0, has_nbrs = True)
        rule2 = MockRule(new_location = self.square40, tiebreak = False)
        rule2.next_rule = self.rule
        knight = tour.Knight(location = location, initial_rule = rule2)

        out = MockFile()
        knight.move()
        knight.write_current_data(out)
        self.assertEquals("{'square':(4,0), 'tiebreak':False}", out.s)

        out = MockFile()
        knight.move()
        knight.write_current_data(out)
        self.assertEquals("{'square':(2,1), 'tiebreak':False}", out.s)

        out = MockFile()
        knight.move()
        knight.write_current_data(out)
        self.assertEquals("{'square':(2,1), 'tiebreak':False}", out.s)

    def testMoveUpdatesTiebreak(self):
        location = MockSquare(x = 0, y = 0, has_nbrs = True)
        self.square33 = MockSquare(x = 3, y = 3, has_nbrs = True)
        rule2 = MockRule(new_location = self.square33, tiebreak = True)
        knight = tour.Knight(location = location, initial_rule = rule2)

        out = MockFile()
        knight.move()
        knight.write_current_data(out)
        self.assertEquals("{'square':(3,3), 'tiebreak':True}", out.s)
        
class MockSquare:
    def __init__(self, x, y, has_nbrs):
        (self.x, self.y, self.has_nbrs) = (x, y, has_nbrs)
        self.visited = False
    def __str__(self):
        return "(%d,%d)" % (self.x, self.y)
    def has_no_neighbours(self):
        return (not self.has_nbrs)

class MockRule:
    def __init__(self, new_location, tiebreak):
        self.new_location = new_location
        self.next_rule = self
        self.tiebreak = tiebreak
    def invoke(self, square):
        self.invoked_on = square
        return [self.new_location, self.tiebreak, self.next_rule] 

class MockFile:
    def __init__(self):
        self.s = ""
    def write(self, data):
        self.s += data

if __name__ == '__main__':
    unittest.main()
