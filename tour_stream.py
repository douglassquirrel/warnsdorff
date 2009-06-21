class TourStream:
    def __init__(self, file):
        self.file = file
        self.dimension = int(file.next())
    def __iter__(self):
        return self
    def next(self):
        return eval(self.file.next())
