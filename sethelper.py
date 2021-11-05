from PIL import Image, ImageDraw, ImageFont
import textwrap
import math

cardsize = cardwidth, cardheight = 825, 1125 # poker deck on thegamecrafter.com
cardcenter = cardwidth/2,cardheight/2

## utility functions to help draw
# polar coordinates from given center, using degrees
polar = lambda p,r,t: (p[0]+math.cos(t/180*math.pi)*r, p[1]+math.sin(t/180*math.pi)*r)
# bounding squares with given radius for e.g. draw.ellipse
bounding_box = lambda p,r: [p[0]-r, p[1]-r, p[0]+r, p[1]+r]

def blankcard(color=(255,255,255)):
	img = Image.new("RGB", cardsize, color)
	draw = ImageDraw.Draw(img)
	return img, draw

orienter_size = 200
def draw_orienter(draw):
	draw.polygon([(0,0), (0,orienter_size), (orienter_size,0)], (0,0,0))

def setback(text, color, orienter=True):
	midw, midh = 201, 501 # should be odd
	rounding = 50
	img, draw = blankcard(color)

	draw.rounded_rectangle([cardwidth/2-midw/2-rounding, cardheight/2-midh/2-rounding, cardwidth/2+midw/2+rounding, cardheight/2+midh/2+rounding], rounding, (255,255,255))

	drawh, draww = midh + rounding*2, midw + rounding*2
	d = ImageDraw.Draw(txt := Image.new("L", [drawh, draww], 0))
	d.text([(drawh)/2, (draww)/2], text, 255, ImageFont.truetype("Ubuntu-M.ttf", 200), "mm")
	img.paste(Image.new("L",[draww, drawh],0), [(cardwidth-draww)//2, (cardheight-drawh)//2], mask=txt.rotate(90, expand=True, fillcolor=255))

	if orienter: draw.polygon([(cardwidth,0), (cardwidth,orienter_size), (cardwidth-orienter_size, 0)], (0,0,0))

	return img


def textcard(parts):
	chars = 37
	lines = sum(len(textwrap.wrap(p,chars))+1 for p in parts)-1
	left = 90
	fontsize = 35
	top = (cardheight - lines * fontsize)/2
	font = ImageFont.truetype("UbuntuMono-R.ttf", fontsize)
	img, draw = blankcard()

	for p in parts:
		for t in textwrap.wrap(p, chars):
			draw.text([left, top], t, (0,0,0), font, "lt")
			top += fontsize
		top += fontsize

	return img
