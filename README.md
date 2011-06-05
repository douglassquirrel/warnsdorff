[Warnsdorff's Rule](http://warnsdorff.com) is a heuristic for finding knight's tours on chessboards. A [conjecture](https://github.com/douglassquirrel/warnsdorff/blob/master/5_Squirrel96.pdf?raw=true) by the original contributor of this code and [Paul Cull](http://eecs.oregonstate.edu/research/members/cull/index.html) is that Warnsdorff's rule, with suitable modifications, can give a knight's tour on any square board. You can use this program to generate tours according to this method on a square board of any size:

1. Download this project.
2. Follow the instructions in the INSTALL file (installing Python and required libraries).
3. Type `python tour.py 100` to produce instructions for a tour on a board of size 100.
4. Type `python tour.py 100 | python tour_to_tk.py` to see the tour drawn for you in a [TkInter](http://wiki.python.org/moin/TkInter) window.
5. Type `python tour.py 100 | python tour_to_swf.py` to get an swf (Flash) movie of the tour being drawn.

When the tour is "drawn" you see a square coloured blue or red when the knight reaches that square - blue indicates that no tiebreak was necessary, red that a tiebreak was needed (see the research paper cited above for more details).

I hope that users of this code are inspired to learn more about Warnsdorff's Rule, and perhaps to prove that the modified rule will actually produce tours on all square boards - this is known for boards whose size is equivalent to 7 mod 8, thanks to [Sam Ganzfried's REU paper on the subject](https://github.com/douglassquirrel/warnsdorff/blob/master/SGKnightsTourPaper.pdf?raw=true).

