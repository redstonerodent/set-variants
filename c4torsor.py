from sethelper import *

colors = [(255,0,0), (240,210,0), (0,255,0)]
diam = 300  # diameter
sep = 360 # distance between clocks
hands = [(0, -diam/2), (diam/2, 0), (0, diam/2), (-diam/2, 0)]


for n in range(64):
	img, draw = blankcard()
	draw_orienter(draw)
	for i,c in enumerate(colors):
		draw.ellipse([(cardwidth-diam)/2, (cardheight-diam)/2+(i-1)*sep, (cardwidth+diam)/2, (cardheight+diam)/2+(i-1)*sep], None, c, 20)
		hx, hy = hands[(n>>2*i)%4]
		draw.line([cardwidth/2, cardheight/2+(i-1)*sep, cardwidth/2+hx, cardheight/2+(i-1)*sep+hy], c, 30)
	img.save(f'c4torsor/fronts/{n}.png')

setback('C4T3', (250, 50, 50)).save('c4torsor/back.png')
