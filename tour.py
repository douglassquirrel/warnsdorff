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
        self.location = location
        self.rule = initial_rule
        self.tiebreak = False

    def write_current_data(self, out):
        out.write("{'square':%s, 'tiebreak':%s}" % (self.location.serialise(), self.tiebreak))

    def move(self):
        if (self.location.has_no_neighbours()):
            return False
        (self.location, self.rule, self.tiebreak) = self.rule.invoke(square = self.location)
        return True
