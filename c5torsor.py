from sethelper import *
import math

colors = [(255,0,0), (240,210,0), (0,255,0)]
diam = 300  # diameter
sep = 360 # distance between clocks
hands = [(math.sin(math.pi*2/5*i)*diam/2, -math.cos(math.pi*2/5*i)*diam/2) for i in range(5)]


for n in range(5**3):
	img, draw = blankcard()
	draw_orienter(draw)
	for i,c in enumerate(colors):
		draw.ellipse([(cardwidth-diam)/2, (cardheight-diam)/2+(i-1)*sep, (cardwidth+diam)/2, (cardheight+diam)/2+(i-1)*sep], None, c, 20)
		hx, hy = hands[(n//(5**i))%5]
		draw.line([cardwidth/2, cardheight/2+(i-1)*sep, cardwidth/2+hx, cardheight/2+(i-1)*sep+hy], c, 30)
	img.save(f'c5torsor/fronts/{n}.png')

setback('C5T3', (255, 0, 255)).save('c5torsor/back.png')
