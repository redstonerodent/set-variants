from sethelper import *
import math
import random

folder = 'c5torsor'

pentagons = [(255,0,0), (0,255,0), (0,0,255)]
pent_rad = 140  # radius of pentagons
dot_rad = 25 # radius of dots
sep = 330 # distance between clocks
thickness = 30 # of pentagon lines
colors = [(255,153,0), (51,255,0), (0,255,255), (51,0,255), (255,0,153)]

def drawpentagon(draw, cx, cy, inr, outr, theta, n, color):
	# draws pentagon on draw with
	# center cx,cy
	# inner radius inr
	# outner radius outr
	# rotated by theta
	# position n (0-4)
	# vertices color
	x = lambda i, r=outr: cx+math.sin(theta+math.pi*2/5*i)*r
	y = lambda i, r=outr: cy+math.cos(theta+math.pi*2/5*i)*r

	draw.line([(x(i), y(i)) for i in range(7)], (0,0,0), 20, 'curve')
	for i,c in enumerate(colors):
		draw.ellipse([x(i)-dot_rad, y(i)-dot_rad, x(i)+dot_rad, y(i)+dot_rad], c)
	draw.line([x(n), y(n), x(n,inr), y(n,inr), x(n), y(n)], colors[n], thickness, 'curve')
	draw.ellipse([x(n,inr)-dot_rad, y(n,inr)-dot_rad, x(n,inr)+dot_rad, y(n,inr)+dot_rad], colors[n])
	# draw.polygon([x(n+1,inr), y(n+1,inr), x(n,inr), y(n,inr), x(n), y(n), x(n+1), y(n+1)], colors[n])

	# hx, hy = math.sin(theta+math.pi*2/5*n)*r, math.cos(theta+math.pi*2/5*n)*r
	# draw.ellipse([cx+hx-dot_rad, cy+hy-dot_rad, cx+hx+dot_rad, cy+hy+dot_rad], c, (0,0,0), 4)



for n in range(5**3):
	img, draw = blankcard()
	draw_orienter(draw)
	for i,c in enumerate(pentagons):
		theta = 0
		# theta = random.random()
		drawpentagon(draw, cardwidth/2, cardheight/2+(i-1)*sep, 0, pent_rad, theta, (n//(5**i))%5, c)
		# drawpentagon(draw, cardwidth/2, cardheight/2, pent_rad*(2-i), pent_rad*(3-i), theta, (n//(5**i))%5, c)
	img.save(f'{folder}/fronts/{n}.png')

setback('C53T', (255, 0, 255)).save(f'{folder}/back.png')

textcard([
	'Welcome to C53T, a Set-like game!',
	'Cards: 125',
	'Difficulty: Hard',
	'Suggested Deal: 12',
	'Guarantees Set: Unknown',
	'Set Size: 5',
	'Sets: In each color, the five directions must have a line of symmetry. Equivalently, all five in the same direction is valid, and rotating one arm one step clockwise and another arm one step counterclockwise preserves validity.',
	'Math: Torsor for C_5^3',
	]).save(f'{folder}/fronts/rules.png')