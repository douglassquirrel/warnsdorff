import Image
import ImageDraw
import ImageTk
import subprocess
import sys
import Tkinter
import tour_stream

def flip(p):
    return (p[1], p[0])

def next_frame(stream, label, im, draw):
    try:
        datum = stream.next()
    except StopIteration:
        return
    draw.point(flip(datum["square"]), \
               fill = "red" if datum["tiebreak"] else "blue")

    frame = ImageTk.PhotoImage(im) 
    label.config(image=frame)
    label.image = frame
    label.pack()   
    label.master.after(1, next_frame, stream, label, im, draw)

stream = tour_stream.TourStream(sys.stdin)
n = stream.dimension

im = Image.new("RGB", (n+1, n+1))
draw = ImageDraw.Draw(im)
draw.rectangle((0, 0, n+1, n+1), fill="white")

root = Tkinter.Tk()
frame = ImageTk.PhotoImage(im)
label = Tkinter.Label(root, image=frame)
label.pack()
root.after(1, next_frame, stream, label, im, draw)
root.mainloop()
