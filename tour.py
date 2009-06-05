CANNOT_MOVE = False
class Generator:
    def __init__(self, knight):
        self.knight = knight

    def run(self, out):
        while True:
            self.knight.write_current_data(out)
            if (self.knight.move() == CANNOT_MOVE):
                break
