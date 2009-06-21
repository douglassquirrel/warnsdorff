import cStringIO
import tour_stream
import unittest

class TourStreamTest(unittest.TestCase):
    TOUR_DATA = \
["3",\
"{'square':(1,1), 'tiebreak':False}",\
"{'square':(2,3), 'tiebreak':True}" ,\
"{'square':(3,1), 'tiebreak':False}",\
"{'square':(1,2), 'tiebreak':False}",\
"{'square':(3,3), 'tiebreak':False}",\
"{'square':(2,1), 'tiebreak':False}",\
"{'square':(1,3), 'tiebreak':False}",\
"{'square':(3,2), 'tiebreak':False}",]

    def setUp(self):
        tour_file = cStringIO.StringIO("\n".join(self.TOUR_DATA))
        self.stream = tour_stream.TourStream(file = tour_file)    

    def testReportsDimension(self):
        self.assertEquals(3, self.stream.dimension)

    def testReadsData(self):
        i = 0
        for square_datum in self.stream:
            i += 1
            self.assertEquals(eval(self.TOUR_DATA[i]), square_datum)

if __name__ == '__main__':
    unittest.main()
