from sethelper import *
import math
import random

folder = 'c5torsor'

pentagons = [(0,0,0), (100,100,100), (160,160,160)]
pent_rad = 140  # radius of pentagons
dot_rad = 25 # radius of dots
sep = 310 # distance between clocks
thickness = 30 # of pentagon lines
colors = [(255,0,0), (240,150,0), (0,220,0), (0,0,255), (155,0,255)]
outline = 5 # width of outline

def drawpentagon(draw, cx, cy, inr, outr, theta, n, color, linewidth):
	# draws pentagon on draw with
	# center cx,cy
	# inner radius inr
	# outner radius outr
	# rotated by theta
	# position n (0-4)
	# vertices color
	# spoke has width linewidth
	x = lambda i, r=outr: cx+math.sin(theta+math.pi*2/5*i)*r
	y = lambda i, r=outr: cy+math.cos(theta+math.pi*2/5*i)*r

	draw.line([x(n), y(n), x(n,inr), y(n,inr)], color, thickness + 2*outline)
	draw.line([(x(i), y(i)) for i in range(7)], color, linewidth, 'curve')
	draw.ellipse([x(n,inr)-dot_rad, y(n,inr)-dot_rad, x(n,inr)+dot_rad, y(n,inr)+dot_rad], colors[n], color, outline)
	for i,c in enumerate(colors):
		draw.ellipse([x(i)-dot_rad, y(i)-dot_rad, x(i)+dot_rad, y(i)+dot_rad], c, color, outline)
	draw.line([x(n), y(n), x(n,inr), y(n,inr), x(n), y(n)], colors[n], thickness, 'curve')

for n in range(5**3):
	img, draw = blankcard()
	draw_orienter(draw)
	for i,c in enumerate(pentagons):
		drawpentagon(draw, cardwidth/2, cardheight/2+(i-1)*sep, 0, pent_rad, 0, (n//(5**i))%5, c, 20)
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