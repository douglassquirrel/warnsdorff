CANNOT_MOVE = False
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
