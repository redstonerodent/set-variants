from sethelper import *
import math

colors = [(255,0,0), (240,210,0), (0,255,0)]
diam = 280  # diameter
sep = 300 # distance between clocks
vertices = [(math.sin(math.pi*2/5*i)*diam/2, -math.cos(math.pi*2/5*i)*diam/2) for i in range(7)]


for n in range(5**3):
	img, draw = blankcard()
	draw_orienter(draw)
	for i,c in enumerate(colors):
		draw.line([(cardwidth/2+x, cardheight/2+(i-1)*sep+y) for x,y in vertices], c, 20, 'curve')
		hx, hy = vertices[(n//(5**i))%5]
		draw.line([cardwidth/2, cardheight/2+(i-1)*sep, cardwidth/2+hx, cardheight/2+(i-1)*sep+hy], c, 30)
	img.save(f'c5torsor/fronts/{n}.png')

setback('C53T', (255, 0, 255)).save('c5torsor/back.png')

(cardwidth-diam)/2, (cardheight-diam)/2+(i-1)*sep