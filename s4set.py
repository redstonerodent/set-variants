from PIL import Image, ImageDraw, ImageFont
from itertools import permutations

width, height = 825, 1125 # for poker deck

dist = 221 # distance between endpoints (should be odd)
y = height/2-dist/2-dist # position of top endpoint

for order in permutations(range(4)):
	draw = ImageDraw.Draw(img := Image.new("RGB", (width,height), (255,255,255)))
	for i,j in enumerate(order):
		draw.line([0, y+i*dist, width, y+j*dist], (0,0,0), 10)
	img.save(f's4set/fronts/{order}.png')