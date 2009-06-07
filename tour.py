import config
import sys

def get_mins(L, scorer):
    minimum = min(map(scorer, L))
    return [item for item in L if scorer(item) == minimum]

CANNOT_MOVE = False
class Generator:
    def __init__(self, knight):
        self.knight = knight
        knight.location.visited = True

    def run(self, out):
        visited = 0
        while True:
            visited += 1
            self.knight.write_current_data(out)
            out.write("\n")
            if (self.knight.move() == CANNOT_MOVE):
                break
        return visited

class Knight:
    def __init__(self, location, initial_rule):
        (self.location, self.rule, self.tiebreak) = (location, initial_rule, False)

    def write_current_data(self, out):
        out.write("{'square':%s, 'tiebreak':%s}" % (str(self.location), self.tiebreak))

    def move(self):
        if (self.location.has_no_neighbours()):
            return False
        (self.location, self.tiebreak, self.rule) = self.rule.invoke(square = self.location)
        self.location.visited = True
        return True

class Rule:
    def __init__(self, ordering, switch_square, next_rule):
        (self.ordering, self.switch_square, self.next_rule) = (ordering, switch_square, next_rule)
    
    def invoke(self, square):
        result = square.pick_neighbour(lambda x : x["square"].degree(), \
                                       lambda x : self.ordering.find(str(x["direction"])))
        result.append(self.next_rule if (square.equals(self.switch_square)) else self)
        return result

class Square:
    def __init__(self, board, x, y):
        (self.board, self.x, self.y) = (board, x, y)
        self.visited = False
    def equals(self, square):
        return (self.x == square.x and self.y == square.y) if square else False
    def __str__(self):
        return "(%d,%d)" % (self.x, self.y)
    def degree(self):
        return len(self.board.get_unvisited_neighbours(self))
    def has_no_neighbours(self):
        return (0 == self.degree())
    def pick_neighbour(self, scorer, tiebreaker):
        candidates = get_mins(self.board.get_unvisited_neighbours(self), scorer)
        if (1 == len(candidates)):
            return [candidates[0]["square"], False]
        else:
            return [get_mins(candidates, tiebreaker)[0]["square"], True]

class Board:
    def __init__(self, dim):
        self.dim = dim
        self.squares = [[Square(self, x, y) for y in range(0, dim)] for x in range(0, dim)]
        self.directions = [Direction(number=1, x=1,  y=-2), \
                           Direction(number=2, x=2,  y=-1), \
                           Direction(number=3, x=2,  y=1 ), \
                           Direction(number=4, x=1,  y=2 ), \
                           Direction(number=5, x=-1, y=2 ), \
                           Direction(number=6, x=-2, y=1 ), \
                           Direction(number=7, x=-2, y=-1), \
                           Direction(number=8, x=-1, y=-2)]
    def get_square_at(self, x, y):
        return self.squares[x][y] if (x in range(0, self.dim) and y in range(0, self.dim)) else None
    def get_unvisited_neighbours(self, square):
        return filter(lambda x : not x["square"].visited, self.get_neighbours(square))
    def get_neighbours(self, square):
        return [{"direction":d.number, "square":d.apply(square)} for d in self.directions if d.apply(square)]

class Direction:
    def __init__(self, number, x, y):
        (self.number, self.x, self.y) = (number, x, y)
    def apply(self, square):
        return square.board.get_square_at(x = square.x + self.x, y = square.y + self.y)

def run(dim, out):
    board = Board(dim = dim)
    rules = config.get_rules(m = dim, board = board)
    knight = Knight(location = board.get_square_at(x = 0, y = 0), initial_rule = rules[0])
    generator = Generator(knight = knight)
    return generator.run(out)

if __name__ == '__main__':
    run(dim = int(sys.argv[1]), out = sys.stdout)

