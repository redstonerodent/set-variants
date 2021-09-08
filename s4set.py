from sethelper import *
from itertools import permutations

dist = 221 # distance between endpoints (should be odd)
y = cardsize.y/2-dist/2-dist # position of top endpoint
straightlen = 50 # length of horizontal segment

for order in permutations(range(4)):
	draw = ImageDraw.Draw(img := Image.new("RGB", cardsize.coords, (255,255,255)))
	for i,j in enumerate(order):
		draw.line([(0, y+i*dist), (straightlen, y+i*dist), (cardsize.x-straightlen, y+j*dist), (cardsize.x, y+j*dist)], (0,0,0), 10, 'curve')
	img.save(f's4set/fronts/{order}.png')

setback('S4', (50,50,200)).save('s4set/back.png')