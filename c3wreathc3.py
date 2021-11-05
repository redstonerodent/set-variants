from sethelper import *
from itertools import product

folder = 'c3wreathc3'

rad = 270 # radius of big circle
wheel_width = 25
t_rad = 100 # radius of each triangle
rad_adjust = .2*rad # put triangles closer in
width = 10 # outlines
dot_rad = 60

dot_colors = [[(255,0,0), (245,245,0), (0,144,255)], [(240,150,0), (0,180,0), (150,0,255)], [(60,60,60), (255,255,255), (170,170,170)]]
fill_colors = [(111,255,15), (221,19,191), (130,130,130)]


for rotations in product(range(3), repeat=3): # rotations[i] is the rotation the ith triangle
	for wheel in range(3): # rotation of the outer c3
		img, draw = blankcard()
		draw_orienter(draw)

		# big circle
		draw.ellipse(bounding_box(cardcenter,rad), None, (0,0,0), wheel_width)

		for t in range(3): # position we're drawing a triangle
			T = (t+wheel)%3 # which triangle we're drawing
			p = polar(cardcenter, rad-rad_adjust, -90+120*t) # center of triangle

			s = 90 # amount to rotate this triangle
			vertices = [polar(p, t_rad, 120*i+s) for i in range(3)]

			# triangle
			draw.polygon(vertices, fill_colors[T])
			draw.line(vertices*2, (0,0,0), width)

			# dots
			for i,v in enumerate(vertices):
				draw.ellipse(bounding_box(v, dot_rad), dot_colors[T][i], (0,0,0), width)




		img.save(f'{folder}/fronts/{rotations}{wheel}.png')

setback('C3C3', (255,255,0)).save(f'{folder}/back.png')