from sethelper import *
import math

folder = 'creases'


colors = [(255,0,0), (0,0,255)]
thickness = 15
grid_width = 5
grid_color = (200,200,200)
dot_rad = 20

scale = 200
plot = lambda c, r, t: (cardwidth/2 + (c[0]+math.sin(t)*r)*scale, cardheight/2 + (c[1]+math.cos(t)*r)*scale)

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
	(0,1),
	(0,-1),
]
banned = {
	(((0,1),(0,4)), ((0,-1),(0,-4))),
	(((0,1),(3,-2)), ((0,-1),(3,2))),
	(((0,1),(-3,-2)), ((0,-1),(-3,2))),
}


for i in range(1,6): # crease 1 dir
	for j in [4,5,0,1,2]: # crease 2 dir
		for p in range(4): # assignment
			if (i,j,p) in banned: continue

			img, draw = blankcard()

			for d in range(6):
				for y in [-1,1]:
					draw.line([plot((0,y), 0, 0), plot((0,y), 3, math.pi/3*i)], (grid_color), grid_width)
			
			# draw.line(list(map(plot, c1*2)), (0,0,0), thickness, joint='curve')
			# draw.line(list(map(plot, c2*2)), (0,0,0), thickness, joint='curve')
			# draw.line(list(map(plot, [(0,1),(0,-1)]*2)), (0,0,0), thickness, joint='curve')

			draw_orienter(draw)
			img.save(f'{folder}/fronts/{i}-{j}.png')

