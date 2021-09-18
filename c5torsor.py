from sethelper import *
import math

folder = 'c5torsor'

colors = [(255,0,0), (0,255,0), (0,0,255)]
diam = 280  # diameter of pentagons
rad = 40 # radius of dots
sep = 330 # distance between clocks
thickness = 30 # of arms
vertices = [(math.sin(math.pi*2/5*i)*diam/2, -math.cos(math.pi*2/5*i)*diam/2) for i in range(7)]



for n in range(5**3):
	img, draw = blankcard()
	draw_orienter(draw)
	for i,c in enumerate(colors):
		draw.line([(cardwidth/2+x, cardheight/2+(i-1)*sep+y) for x,y in vertices], c, 20, 'curve')
		hx, hy = vertices[(n//(5**i))%5]
		draw.line([cardwidth/2+hx, cardheight/2+(i-1)*sep+hy, cardwidth/2, cardheight/2+(i-1)*sep, cardwidth/2+hx, cardheight/2+(i-1)*sep+hy], (0,0,0), thickness, 'curve')
		draw.ellipse([cardwidth/2+hx-rad, cardheight/2+(i-1)*sep+hy-rad, cardwidth/2+hx+rad, cardheight/2+(i-1)*sep+hy+rad], c, (0,0,0), 4)
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