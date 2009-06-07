import Image
import ImageDraw
import subprocess
import sys

n = int(sys.argv[1])
im = Image.new("RGB", (n, n))
draw = ImageDraw.Draw(im)

draw.rectangle((0, 0, n, n), fill="white")
im.save("tour0.gif")

files = []
i=0
while True:
    line = sys.stdin.readline().rstrip()
    if not line:
        break
    data = eval(line)
    fill = "red" if data["tiebreak"] else "blue"
    draw.point(data["square"], fill = fill)
    i+=1
    filename = "tour%d.gif" % (i,)
    im.save(filename)
    files.append(filename)

command = ["convert", "-delay", "1", "-loop", "0"]
command.extend(files)
command.append("tour.gif")
subprocess.call(command)
