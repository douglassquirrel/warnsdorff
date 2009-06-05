import Image
import ImageDraw
import subprocess
import sys

n = int(sys.argv[1])
print "Generating tour for %d by %d square" % (n, n)
im = Image.new("RGB", (n, n))
draw = ImageDraw.Draw(im)

print "Generating frames..."
draw.rectangle((0, 0, n, n), fill="white")
im.save("king0.gif")

files = []
for i in range(0, n):
    for j in range(0, n):
        draw.point((i, j), fill="red")
        filename = "king%d.gif" % (i*n+j+1,)
        im.save(filename)
        files.append(filename)

command = ["convert", "-delay", "1", "-loop", "0"]
command.extend(files)
command.append("king.gif")
print "Calling imagemagick..."
subprocess.call(command)
