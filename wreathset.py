from sethelper import *
from itertools import permutations

dist = 251 # distance between endpoints (should be odd)
y = cardheight/2-dist # position of top endpoint
straightlen = 90 # length of horizontal segment
rad = 50 # radius of dots
gap = 90 # distance from dot center to edge

for order in permutations(range(3)):
	for dots in range(8):
		img, draw = blankcard()
		draw_orienter(draw)
		for i,j in enumerate(order):
			draw.line([(0, y+i*dist), (straightlen, y+i*dist), (cardwidth-straightlen, y+j*dist), (cardwidth, y+j*dist)], (0,0,0), 10, 'curve')
		for i in range(3):
			if dots>>i&1:
				tx, ty = cardwidth-gap, y+i*dist
				draw.ellipse([tx-rad, ty-rad, tx+rad, ty+rad], outline=(0,0,0), width=10)
		img.save(f'wreathset/fronts/{order}{dots}.png')

setback('WRE', (50,200,50)).save('wreathset/back.png')