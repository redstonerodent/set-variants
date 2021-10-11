from sethelper import *
from itertools import permutations
import math

folder = 'dodecahedron'

thickness = 10 # black lines
gap = 3 # white gaps
sep = 500 # between dodecahedron and icosahedron
dotrad = 50
dotsep = 120 # between centers of dots
dotoutline = 5

### dodecahedron drawing

# positions of dodecahedron points
d_inner_rad = 120
d_outer_rad = 1.5 * d_inner_rad # todo

dodecahodron_colors = {# indexed by magic numbers from order_to_color
	 6: (255,0,0),
	11: (0,255,0),
	14: (0,0,255),
	19: (255,255,0),
	21: (255,0,255),
	24: (0,255,255),
}

x = lambda r, t: cardwidth/2+math.sin(t)*r
dy = lambda r, t: cardheight/2-sep/2+math.cos(t)*r
dp = lambda r, t: (x(r,t), dy(r,t))

# (coordinates of pentagon, permutation of inscribed cube edges
# by fiat, middle face is the identity
dodecahedron_faces = [
	([dp(d_inner_rad, math.pi/5*2*i) for i in range(5)], [0,1,2,3,4]),
	*[
		([
			dp(d_inner_rad, math.pi/5*2*i), dp(d_inner_rad, math.pi/5*2*(i+1)), dp(d_outer_rad, math.pi/5*2*(i+1)), dp(d_outer_rad, math.pi/5*(2*i+1)), dp(d_outer_rad, math.pi/5*2*i)],
			[(i+[0,2,1,4,3][(j-i)%5])%5 for j in range(5)])
		for i in range(5)
	]
]


# for a face of the dodecahdron,
# given p = [position of the diagonal on this face that's part of cube i for i in range(5)]
# return a number that depends on the equivalence class under the necklace group
# this tells you which face it is (up to opposites)
order_to_color = lambda p: ((p[1]-p[0])%5 + 4*((p[2]-p[0])%5))**2 % 25

### icosahedron drawing


icosahedron_colors = [
	(255,0,0),
	(0,255,0),
	(0,0,255),
	(255,255,0),
	(255,0,255),
]


iy = lambda r, t: cardheight/2+sep/2+math.cos(t)*r
ip = lambda r, t: (x(r,t), iy(r,t))


# time to make the cards
for position in permutations(range(5)): # position[i] is the position of color i, or of the ith inscribed cube
	# skip odd permutations
	if sum(position[i]>position[j] for i in range(5) for j in range(i,5))%2: continue

	img, draw = blankcard()
	draw_orienter(draw)

	# draw dodecahedron
	for pentagon, permutation in dodecahedron_faces:
		draw.polygon(pentagon, dodecahodron_colors[order_to_color([permutation[position[i]] for i in range(5)])])
	# outlines
	for pentagon, _ in dodecahedron_faces:
		draw.line(pentagon*2, (255,255,255), thickness+2*gap, 'curve')
	for pentagon, _ in dodecahedron_faces:
		draw.line(pentagon*2, (0,0,0), thickness, 'curve')

	# # white gaps
	# for i in range(3):
	# 	draw.line([cp(0,0), cp(hexrad, math.pi/3*(2*i-1)), cp(hexrad, math.pi/3*(2*i)), cp(hexrad, math.pi/3*(2*i+1)), cp(0,0)], (255,255,255), thickness+2*gap, 'curve')
	# # black lines
	# for i in range(3):
	# 	draw.line([cp(0,0), cp(hexrad, math.pi/3*(2*i-1)), cp(hexrad, math.pi/3*(2*i)), cp(hexrad, math.pi/3*(2*i+1)), cp(0,0)], (0,0,0), thickness, 'curve')
	
	# # draw octahedron
	# draw.polygon([op(hexrad, math.pi/3*2*i) for i in range(3)], octahedoncolors[colorvertex(dots)])
	# for i in range(3):
	# 	draw.polygon([op(hexrad, math.pi/3*(2*i-1)+math.pi), op(hexrad, math.pi/3*(2*i)+math.pi), op(hexrad, math.pi/3*(2*i+1)+math.pi)], octahedoncolors[colorvertex(dots^(2**order.index(i)))])
	# # white gaps
	# draw.line([op(hexrad, math.pi/3*i) for i in range(8)], (255,255,255), thickness+2*gap, 'curve')
	# draw.line([op(hexrad, math.pi/3*2*i) for i in range(5)], (255,255,255), thickness+2*gap, 'curve')
	# # black lines
	# draw.line([op(hexrad, math.pi/3*i) for i in range(8)], (0,0,0), thickness, 'curve')
	# draw.line([op(hexrad, math.pi/3*2*i) for i in range(5)], (0,0,0), thickness, 'curve')

	# draw permutation dots
	for i,color in enumerate(dot_colors):
		# I think this is the backwards permutation right now
		draw.ellipse([cardwidth/2-(2-position[i])*dotsep-dotrad, cardheight/2-dotrad, cardwidth/2-(2-position[i])*dotsep+dotrad, cardheight/2+dotrad], color, (0,0,0), dotoutline)




	img.save(f'{folder}/fronts/{position}.png')

setback('OCTA', (50,200,50)).save(f'{folder}/back.png')