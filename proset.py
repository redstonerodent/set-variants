from PIL import Image, ImageDraw, ImageFont, __version__

print(__version__)

width, height = 825, 1125 # for poker deck

colors = [(255,0,0), (255,255,0), (0,255,0), (0,255,255), (0,0,255), (255,0,255)] # in reading order
diam = 261 # diameter (should be odd)
dist = 320 # dist between circles' centers (should be even)
x, y = width/2-dist/2-diam/2, height/2-dist-diam/2 # position of top left corner of bounding box of top left circle


for n in range(1,64):
	draw = ImageDraw.Draw(img := Image.new("RGB", (width,height), (255,255,255)))
	for i,c in enumerate(colors):
		if n>>i&1:
			draw.ellipse([x+dist*(i%2), y+dist*(i//2), x+dist*(i%2)+diam, y+dist*(i//2)+diam], c, (0,0,0), 5)
	img.save(f'proset/fronts/{n}.png')

# back
midw, midh = 201, 501 # should be odd
rounding = 50
draw = ImageDraw.Draw(img := Image.new("RGB", (width, height), (255,153,0)))
draw.rounded_rectangle([(width-midw)/2-50, (height-midh)/2-50, (width+midw)/2+50, (height+midh)/2+50], rounding, (255,255,255))

d = ImageDraw.Draw(txt := Image.new("L", (midh, midw), 255))
d.text([midh/2, midw/2], 'PRO', 0, ImageFont.truetype("Ubuntu-M.ttf", 200), "mm")
img.paste(txt.rotate(90, expand=True, fillcolor=255), [(width-midw)//2, (height-midh)//2])

img.save('proset/back.png')