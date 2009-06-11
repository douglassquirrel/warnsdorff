import ming
import sys

def make_point(red, green, blue):
    point = ming.SWFShape()
    point.setLine(1, red, green, blue)
    point.drawLineTo(0,1)
    point.drawLineTo(1,1)
    point.drawLineTo(1,0)
    point.drawLineTo(0,0)
    return point

n = int(sys.argv[1])
blue_point = make_point(0, 0, 0xff)
red_point = make_point(0xff, 0, 0)
movie = ming.SWFMovie()
movie.setDimension(n*2, n*2)
movie.setRate(128.0)

while True:
    line = sys.stdin.readline().rstrip()
    if not line:
        break
    data = eval(line)

    point = red_point if data["tiebreak"] else blue_point
    handle = movie.add(point).moveTo(data["square"][1]*2, data["square"][0]*2)
    movie.nextFrame()

movie.save("tour%d.swf" % (n,))
