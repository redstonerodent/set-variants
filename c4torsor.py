from sethelper import *
import math
import random

folder = 'c4torsor'

squares = [(0,0,0), (100,100,100), (160,160,160)]
pent_rad = 140  # radius of squares
dot_rad = 25 # radius of dots
sep = 310 # distance between clocks
thickness = 30 # of square lines
colors = [(255,0,0), (0,220,0), (240,150,0), (0,0,255)]
outline = 5 # width of outline

def drawsquare(draw, cx, cy, inr, outr, theta, n, color, linewidth):
	# draws square on draw with
	# center cx,cy
	# inner radius inr
	# outner radius outr
	# rotated by theta
	# position n (0-4)
	# vertices color
	# spoke has width linewidth
	x = lambda i, r=outr: cx+math.sin(theta+math.pi*2/4*(i+1/2))*r
	y = lambda i, r=outr: cy+math.cos(theta+math.pi*2/4*(i+1/2))*r

	draw.line([x(n), y(n), x(n,inr), y(n,inr)], color, thickness + 2*outline)
	draw.line([(x(i), y(i)) for i in range(7)], color, linewidth, 'curve')
	draw.ellipse([x(n,inr)-dot_rad, y(n,inr)-dot_rad, x(n,inr)+dot_rad, y(n,inr)+dot_rad], colors[n], color, outline)
	for i,c in enumerate(colors):
		draw.ellipse([x(i)-dot_rad, y(i)-dot_rad, x(i)+dot_rad, y(i)+dot_rad], c, color, outline)
	draw.line([x(n), y(n), x(n,inr), y(n,inr), x(n), y(n)], colors[n], thickness, 'curve')

for n in range(4**3):
	img, draw = blankcard()
	draw_orienter(draw)
	for i,c in enumerate(squares):
		drawsquare(draw, cardwidth/2, cardheight/2+(i-1)*sep, 0, pent_rad, 0, (n//(4**i))%4, c, 20)
	img.save(f'{folder}/fronts/{n}.png')

setback('C43T', (250, 50, 50)).save(f'{folder}/back.png')
