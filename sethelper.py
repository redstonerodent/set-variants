from PIL import Image, ImageDraw, ImageFont
import textwrap

cardsize = cardwidth, cardheight = 825, 1125 # poker deck on thegamecrafter.com

def blankcard(color=(255,255,255)):
	img = Image.new("RGB", cardsize, color)
	draw = ImageDraw.Draw(img)
	return img, draw

orienter_size = 200
def draw_orienter(draw):
	draw.polygon([(0,0), (0,orienter_size), (orienter_size,0)], (0,0,0))

def setback(text, color):
	midw, midh = 201, 501 # should be odd
	rounding = 50
	img, draw = blankcard(color)

	draw.rounded_rectangle([cardwidth/2-midw/2-rounding, cardheight/2-midh/2-rounding, cardwidth/2+midw/2+rounding, cardheight/2+midh/2+rounding], rounding, (255,255,255))

	d = ImageDraw.Draw(txt := Image.new("L", [midh, midw], 255))
	d.text([midh/2, midw/2], text, 0, ImageFont.truetype("Ubuntu-M.ttf", 200), "mm")
	img.paste(txt.rotate(90, expand=True, fillcolor=255), [(cardwidth-midw)//2, (cardheight-midh)//2])

	draw.polygon([(cardwidth,0), (cardwidth,orienter_size), (cardwidth-orienter_size, 0)], (0,0,0))

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
