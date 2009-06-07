import Image
import ImageDraw
import subprocess
import sys

def flip(p):
    return (p[1], p[0])

n = int(sys.argv[1])
im = Image.new("RGB", (n, n))
draw = ImageDraw.Draw(im)
draw.rectangle((0, 0, n, n), fill="white")

files = []
i=0
while True:
    filename = "tour%d.gif" % (i,)
    im.save(filename)
    files.append(filename)
    i+=1

    line = sys.stdin.readline().rstrip()
    if not line:
        break
    data = eval(line)
    draw.point(flip(data["square"]), \
               fill = "red" if data["tiebreak"] else "blue")

command = ["convert", "-delay", "1", "-loop", "0"]
command.extend(files)
command.append("tour.gif")
subprocess.call(command)
