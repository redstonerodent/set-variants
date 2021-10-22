from sethelper import *
import math

folder = 'creases2'


colors = [(255,0,0), (50,50,255)]
thickness = 15
grid_width = 5
grid_color = (240,240,240)
dot_rad = 10

scale = 230
plot = lambda r, t, s=scale: (cardwidth/2 + math.cos(t)*r*s, cardheight/2 + math.sin(t)*r*s)

vertices = [
	(0,0),
]

for s,ps in [(1, [0,3]),(3, range(4)),(5, [1])]: # sector size
	for i in range(10): # direction
		for p in ps: # assignment
			img, draw = blankcard()
			draw_orienter(draw)

			for d in range(10):
				draw.line([plot(0,0), plot(3,math.pi/5*d)]*2, grid_color, grid_width, joint='curve')

			for c,d in enumerate([i, i+s]):
				draw.line([plot(0,0), plot(3,math.pi/5*d)]*2, colors[p>>c&1], thickness, joint='curve')

			draw.ellipse([cardwidth/2-dot_rad, cardheight/2-dot_rad, cardwidth/2+dot_rad, cardheight/2+dot_rad], (0,0,0))

			img.save(f'{folder}/fronts/{s}{i}{p}.png')


setback('FO1D', (30,0,30)).save(f'{folder}/back.png')
