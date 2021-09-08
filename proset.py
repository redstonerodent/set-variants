from sethelper import *

colors = [(255,0,0), (255,127,0), (255,255,0), (0,255,0), (0,0,255), (130,0,170)] # in reading order
diam = 261 # diameter (should be odd)
dist = 320 # dist between circles' centers (should be even)
x, y = cardwidth/2 - dist/2 - diam/2, cardheight/2 - dist - diam/2 # position of top left corner of bounding box of top left circle


for n in range(1,64):
	img, draw = blankcard()
	draw_orienter(draw)
	for i,c in enumerate(colors):
		if n>>i&1:
			tx, ty = x + dist*(i%2), y + dist*(i//2)
			draw.ellipse([tx, ty, tx+diam, ty+diam], c, (0,0,0), 5)
	img.save(f'proset/fronts/{n}.png')

setback('PRO', (255,153,0)).save('proset/back.png')