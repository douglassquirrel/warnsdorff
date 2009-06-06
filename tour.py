CANNOT_MOVE = False
def get_mins(L, scorer):
    minimum = min(map(scorer, L))
    return [item for item in L if scorer(item) == minimum]

class Generator:
    def __init__(self, knight):
        self.knight = knight

    def run(self, out):
        out.write("tour=[")
        while True:
            self.knight.write_current_data(out)
            out.write(",")
            if (self.knight.move() == CANNOT_MOVE):
                break
        out.write("]")

class Knight:
    def __init__(self, location, initial_rule):
        (self.location, self.rule, self.tiebreak) = (location, initial_rule, False)

    def write_current_data(self, out):
        out.write("{'square':%s, 'tiebreak':%s}" % (self.location.serialise(), self.tiebreak))

    def move(self):
        if (self.location.has_no_neighbours()):
            return False
        (self.location, self.rule, self.tiebreak) = self.rule.invoke(square = self.location)
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
        return (self.x == square.x and self.y == square.y)
    def serialise(self):
        return "(%d,%d)" % (self.x, self.y)
    def degree(self):
        return len(self.board.get_unvisited_neighbours(self))
    def has_no_neighbours(self):
        return (0 == self.degree())
    def pick_neighbour(self, scorer, tiebreaker):
        candidates = get_mins(self.board.get_unvisited_neighbours(self), scorer)
        if (1 == len(candidates)):
            return (candidates[0]["square"], False)
        else:
            return (get_mins(candidates, tiebreaker)[0]["square"], True)
