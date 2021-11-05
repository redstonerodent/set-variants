from sethelper import *
from itertools import permutations, product
import math

folder = 's3wreathc2'

sep = 400 # between centers of triangles
t_rad = 160 # radius of each triangle
width = 10 # dot outlines
dot_rad = 70
spinner_width = 15

dot_colors = [[(255,0,0), (245,245,0), (0,144,255)], [(240,150,0), (0,180,0), (150,0,255)]]
spinner_colors = [(0,0,0), (150,150,150)]

polar = lambda p,r,t: (p[0]+math.cos(t/180*math.pi)*r, p[1]+math.sin(t/180*math.pi)*r)
bounding_box = lambda p,r: [p[0]-r, p[1]-r, p[0]+r, p[1]+r]


def spinner(draw, p, r, theta, sign, width, color):
	for i in range(3):
		t = theta+120*i
		# draw.ellipse(bounding_box(p,20), (0,0,255))
		draw.arc(bounding_box(polar(p,r/2,t), r/2+width/2), *[t,t-180][::(-1)**sign], color, width)


for orders in product(permutations(range(3)), repeat=2): # orders[i] is the permutation of the ith triangle
	for swap in range(2): # says whether triangles are swapped
		img, draw = blankcard()
		draw_orienter(draw)

		for t in range(2): # position we're drawing a triangle
			T = t^swap # which triangle we're drawing
			p = (cardwidth/2, cardheight/2+sep/2*(-1)**t) # center of triangle

			# draw spinner
			sign = sum(orders[T][i]>orders[T][j] for i in range(3) for j in range(i,3))%2
			spinner(draw, p, t_rad, 90+60*t+(-1)**sign*25, sign, spinner_width, spinner_colors[T])

			# draw dots
			for i in range(3):
				draw.ellipse(bounding_box(polar(p, t_rad, 90+60*t+120*i), dot_rad), dot_colors[T][orders[T][i]], (spinner_colors[T]), width)




		img.save(f'{folder}/fronts/{orders}{swap}.png')

setback('S3CT', (209,152,249)).save(f'{folder}/back.png')