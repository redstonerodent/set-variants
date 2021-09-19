from sethelper import *
from itertools import permutations
import math

folder = 'wreathtorsor'

hexrad = 200 # radius of outer hexagon
thickness = 10 # black lines
gap = 10 # white gaps
dotrad = 100 # radius of white circles
width = 30 # outlined rhombi
sep = 450 # between cube and octahedron
parityrad = 60 # parity dot

cubecolors = [(255,0,0), (0,255,0), (0,0,255)]
octahedoncolors = [(155,0,255), (240, 150, 0), (255,0,200), (0,255,255)]

x = lambda r, t: cardwidth/2+math.sin(t)*r
cy = lambda r, t: cardheight/2-sep/2+math.cos(t)*r
cp = lambda r, t: (x(r,t), cy(r,t))

oy = lambda r, t: cardheight/2+sep/2+math.cos(t)*r
op = lambda r, t: (x(r,t), oy(r,t))

bit = lambda b, i: b>>i&1 
# find octahedron color index
colorvertex = lambda dots: 3*(dots>>2)^(dots&3)

for order in permutations(range(3)): # order[j] is the position of color j
	for dots in range(8): # bit(dots, j) says whether color j is outlined
		img, draw = blankcard()
		draw_orienter(draw)

		# draw cube
		for j,i in enumerate(order):
			draw.polygon([cp(0,0), cp(hexrad, math.pi/3*(2*i-1)), cp(hexrad, math.pi/3*(2*i)), cp(hexrad, math.pi/3*(2*i+1))], cubecolors[j])
			if bit(dots, j):
				offsetx, offsety = math.sin(math.pi/3*2*i)*(width+thickness/2+gap), math.cos(math.pi/3*2*i)*(width+thickness/2+gap)
				draw.polygon([
					(x(0,0)+offsetx, cy(0,0)+offsety),
					(x(hexrad, math.pi/3*(2*i-1))+offsety*3**.5, cy(hexrad, math.pi/3*(2*i-1))-offsetx*3**.5),
					(x(hexrad, math.pi/3*(2*i))-offsetx, cy(hexrad, math.pi/3*(2*i))-offsety),
					(x(hexrad, math.pi/3*(2*i+1))-offsety*3**.5, cy(hexrad, math.pi/3*(2*i+1))+offsetx*3**.5),
					], (255,255,255))
		# white gaps
		for i in range(3):
			draw.line([cp(0,0), cp(hexrad, math.pi/3*(2*i-1)), cp(hexrad, math.pi/3*(2*i)), cp(hexrad, math.pi/3*(2*i+1)), cp(0,0)], (255,255,255), thickness+2*gap, 'curve')
		# black lines
		for i in range(3):
			draw.line([cp(0,0), cp(hexrad, math.pi/3*(2*i-1)), cp(hexrad, math.pi/3*(2*i)), cp(hexrad, math.pi/3*(2*i+1)), cp(0,0)], (0,0,0), thickness, 'curve')
		
		# draw octahedron
		draw.polygon([op(hexrad, math.pi/3*2*i) for i in range(3)], octahedoncolors[colorvertex(dots)])
		for i in range(3):
			draw.polygon([op(hexrad, math.pi/3*(2*i-1)+math.pi), op(hexrad, math.pi/3*(2*i)+math.pi), op(hexrad, math.pi/3*(2*i+1)+math.pi)], octahedoncolors[colorvertex(dots^(2**order.index(i)))])
		# white gaps
		draw.line([op(hexrad, math.pi/3*i) for i in range(8)], (255,255,255), thickness+2*gap, 'curve')
		draw.line([op(hexrad, math.pi/3*2*i) for i in range(5)], (255,255,255), thickness+2*gap, 'curve')
		# black lines
		draw.line([op(hexrad, math.pi/3*i) for i in range(8)], (0,0,0), thickness, 'curve')
		draw.line([op(hexrad, math.pi/3*2*i) for i in range(5)], (0,0,0), thickness, 'curve')

		# parity dot
		if bit(dots,0)^bit(dots,1)^bit(dots,2)^(sum(order[i]>order[j] for i in range(3) for j in range(i,3))%2):
			draw.ellipse([x(0,0)-parityrad, oy(0,0)-parityrad, x(0,0)+parityrad, oy(0,0)+parityrad], (0,0,0))

		img.save(f'{folder}/fronts/{order}{dots}.png')

setback('CUBE', (50,200,50)).save(f'{folder}/back.png')