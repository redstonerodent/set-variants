from sethelper import *
from itertools import permutations

dist = 251 # distance between endpoints (should be odd)
y = cardsize.y/2-dist # position of top endpoint
straightlen = 90 # length of horizontal segment
rad = 50 # radius of dots
gap = 90 # distance from dot center to edge

for order in permutations(range(3)):
	for dots in range(8):
		draw = ImageDraw.Draw(img := Image.new("RGB", cardsize.coords, (255,255,255)))
		for i,j in enumerate(order):
			draw.line([(0, y+i*dist), (straightlen, y+i*dist), (cardsize.x-straightlen, y+j*dist), (cardsize.x, y+j*dist)], (0,0,0), 10, 'curve')
		for i in range(3):
			if dots>>i&1:
				t = Point(cardsize.x - gap, y+i*dist)
				draw.ellipse([(t-Point(rad, rad)).coords, (t+Point(rad, rad)).coords], outline=(0,0,0), width=10)
		img.save(f'wreathset/fronts/{order}{dots}.png')

setback('WRE', (50,200,50)).save('wreathset/back.png')