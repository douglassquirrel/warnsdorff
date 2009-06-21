import ming
import sys
import tour_stream

def make_point(red, green, blue):
    point = ming.SWFShape()
    point.setLine(1, red, green, blue)
    point.drawLineTo(0,1)
    point.drawLineTo(1,1)
    point.drawLineTo(1,0)
    point.drawLineTo(0,0)
    return point

stream = tour_stream.TourStream(sys.stdin)
n = stream.dimension
blue_point = make_point(0, 0, 0xff)
red_point = make_point(0xff, 0, 0)
movie = ming.SWFMovie()
movie.setDimension((n+1)*2, (n+1)*2)
movie.setRate(128.0)

for datum in stream:
    point = red_point if datum["tiebreak"] else blue_point
    handle = movie.add(point).moveTo(datum["square"][1]*2, datum["square"][0]*2)
    movie.nextFrame()

movie.save("tour%d.swf" % (n,))
