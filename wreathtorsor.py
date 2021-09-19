from sethelper import *
from itertools import permutations
import math

folder = 'wreathtorsor'

hexrad = 400 # radius of outer hexagon
thickness = 20 # black lines
gap = 15 # white gaps
dotrad = 100 # radius of white circles
width = 70 # outlined rhombi

colors = [(255,0,0), (0,255,0), (0,0,255)]

x = lambda r, t: cardwidth/2+math.sin(t)*r
y = lambda r, t: cardheight/2+math.cos(t)*r
p = lambda r, t: (x(r,t), y(r,t))

for order in permutations(range(3)):
	for dots in range(8):
		img, draw = blankcard()
		draw_orienter(draw)
		for i,j in enumerate(order):
			draw.polygon([p(0,0), p(hexrad, math.pi/3*(2*i-1)), p(hexrad, math.pi/3*(2*i)), p(hexrad, math.pi/3*(2*i+1))], colors[j])
			if dots>>i&1:
				offsetx, offsety = math.sin(math.pi/3*2*i)*(width+thickness/2+gap), math.cos(math.pi/3*2*i)*(width+thickness/2+gap)
				draw.polygon([
					(x(0,0)+offsetx, y(0,0)+offsety),
					(x(hexrad, math.pi/3*(2*i-1))+offsety*3**.5, y(hexrad, math.pi/3*(2*i-1))-offsetx*3**.5),
					(x(hexrad, math.pi/3*(2*i))-offsetx, y(hexrad, math.pi/3*(2*i))-offsety),
					(x(hexrad, math.pi/3*(2*i+1))-offsety*3**.5, y(hexrad, math.pi/3*(2*i+1))+offsetx*3**.5),
					], (255,255,255))
		for i in range(3):
			draw.line([p(0,0), p(hexrad, math.pi/3*(2*i-1)), p(hexrad, math.pi/3*(2*i)), p(hexrad, math.pi/3*(2*i+1)), p(0,0)], (255,255,255), thickness+2*gap, 'curve')
		for i in range(3):
			draw.line([p(0,0), p(hexrad, math.pi/3*(2*i-1)), p(hexrad, math.pi/3*(2*i)), p(hexrad, math.pi/3*(2*i+1)), p(0,0)], (0,0,0), thickness, 'curve')
		img.save(f'{folder}/fronts/{order}{dots}.png')

setback('CUBE', (50,200,50)).save(f'{folder}/back.png')