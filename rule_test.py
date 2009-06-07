import tour
import unittest

class RuleTest(unittest.TestCase):
    def setUp(self):        
        self.new_square = MockSquare(x = 2, y = 1)
        self.square = MockSquare(x = 0, y = 0)
        self.square.neighbour = self.new_square
        self.square.tiebreak = False

    def testSwitchesToNewRuleWhenLandingOnSwitchSquare(self):
        rule2 = tour.Rule(ordering = "12345678", switch_square = None, next_rule = None)
        rule1 = tour.Rule(ordering = "12345678", switch_square = self.square, next_rule = rule2)
        self.assertEquals(rule2, rule1.transition(self.square))

    def testDoesNotSwitchRulesIfNotOnSwitchSquare(self):
        switch_square = MockSquare(x = 5, y = 5)
        rule2 = tour.Rule(ordering = "12345678", switch_square = None, next_rule = None)
        rule1 = tour.Rule(ordering = "12345678", switch_square = switch_square, next_rule = rule2)
        self.assertEquals(rule1, rule1.transition(self.square))

    def testPicksNeighbour(self):
        rule = tour.Rule(ordering = "12345678", switch_square = None, next_rule = None)
        (s, tiebreak) = rule.apply_to(self.square)
        self.assertTrue(self.new_square.equals(s))
        self.assertEquals(False, tiebreak)
        self.square.tiebreak = True
        (s, tiebreak) = rule.apply_to(self.square)
        self.assertEquals(True, tiebreak)

    def testPicksNeighbourUsingCorrectScorer(self):
        rule = tour.Rule(ordering = "12345678", switch_square = None, next_rule = None)
        (s, tiebreak) = rule.apply_to(self.square)
        scorer = self.square.scorer
        self.new_square.deg = 5
        self.assertEquals(5, scorer({"square" : self.new_square}))
        self.new_square.deg = 2
        self.assertEquals(2, scorer({"square" : self.new_square}))

    def testPicksNeighbourUsingCorrectTiebreaker(self):
        rule = tour.Rule(ordering = "87654321", switch_square = None, next_rule = None)
        (s, tiebreak) = rule.apply_to(self.square)
        tiebreaker = self.square.tiebreaker
        self.assertEquals(0, tiebreaker({"direction" : 8}))
        self.assertEquals(5, tiebreaker({"direction" : 3}))
        
        rule = tour.Rule(ordering = "18273645", switch_square = None, next_rule = None)
        (s, tiebreak) = rule.apply_to(self.square)
        tiebreaker = self.square.tiebreaker
        self.assertEquals(1, tiebreaker({"direction" : 8}))
        self.assertEquals(4, tiebreaker({"direction" : 3}))

class MockSquare:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def equals(self, square):
        return (self.x == square.x and self.y == square.y)
    def pick_neighbour(self, scorer, tiebreaker):
        self.scorer = scorer
        self.tiebreaker = tiebreaker
        return [self.neighbour, self.tiebreak]
    def degree(self):
        return self.deg

if __name__ == '__main__':
    unittest.main()
