from sethelper import *

colors = [(255,0,0), (255,255,0), (0,255,0), (0,255,255), (0,0,255), (255,0,255)] # in reading order
diam = 261 # diameter (should be odd)
dist = 320 # dist between circles' centers (should be even)
topleft = cardsize/2 - Point(dist/2+diam/2, dist+diam/2) # position of top left corner of bounding box of top left circle

for n in range(1,64):
	draw = ImageDraw.Draw(img := Image.new("RGB", cardsize.coords, (255,255,255)))
	for i,c in enumerate(colors):
		if n>>i&1:
			t = topleft + Point(dist*(i%2), dist*(i//2))
			draw.ellipse([t.coords, (t+Point(diam,diam)).coords], c, (0,0,0), 5)
	img.save(f'proset/fronts/{n}.png')

setback('PRO', (255,153,0)).save('proset/back.png')