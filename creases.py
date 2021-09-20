from sethelper import *
import math

folder = 'creases'


colors = [(255,0,0), (0,0,255)]
thickness = 15
grid_width = 5
grid_color = (200,200,200)
dot_rad = 20

scale = 230
plot = lambda c, r, t, s=scale: (cardwidth/2 + c[0]*scale + math.sin(t)*r*s, cardheight/2 + c[1]*scale + math.cos(t)*r*s)

creases = [
	((0,1),(0,4)),
	((0,1),(3,4)),
	((0,1),(3,1)),
	((0,1),(3,-2)),
	# ((0,1),(0,-1)),
	((0,1),(-3,-2)),
	((0,1),(-3,1)),
	((0,1),(-3,4)),
	((0,-1),(0,-4)),
	((0,-1),(3,2)),
	((0,-1),(3,-1)),
	((0,-1),(3,-4)),
	((0,-1),(-3,-4)),
	((0,-1),(-3,-1)),
	((0,-1),(-3,2)),
]
vertices = [
	(0,-1),
	(0,1),
]
banned = {
	(3,0,0),
	(3,0,3),
}


for i in range(1,6): # (0,1) dir
	for j in [4,5,0,1,2]: # (0,-1) dir
		for p in range(4): # assignment
			if (i,j,p) in banned: continue

			img, draw = blankcard()
			# draw_orienter(draw)

			# for v in vertices:
			# 	draw.ellipse([plot(v, dot_rad, math.pi*5/4, 1), plot(v, dot_rad, math.pi*1/4, 1)], grid_color)
			# 	for d in range(6):
			# 		draw.line([plot(v, 0, 0), plot(v, 3, math.pi/3*d)], grid_color, grid_width)
			
			for c,(v,d) in enumerate(zip(vertices, [i,j])):
				draw.line([plot(v,0,0), plot(v,3,math.pi/3*d)]*2, colors[p>>c&1], thickness, joint='curve')

			draw.line([plot((0,1),0,0),plot((0,-1),0,0)]*2, (0,0,0), thickness, joint='curve')

			draw.polygon([cardwidth/2, cardheight/2-40, cardwidth/2-40, cardheight/2+40, cardwidth/2+40, cardheight/2+40], (0,0,0))

			img.save(f'{folder}/fronts/{i}{j}{p}.png')


setback('FOLD', (100,0,100)).save(f'{folder}/back.png')
