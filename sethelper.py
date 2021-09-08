from continuousEngine.core.geometry import Point
from PIL import Image, ImageDraw, ImageFont

cardsize = Point(825, 1125) # poker deck on thegamecrafter.com


def setback(text, color):
	midsize = Point(201, 501) # should be odd
	rounding = 50
	draw = ImageDraw.Draw(img := Image.new("RGB", cardsize.coords, color))

	draw.rounded_rectangle([(cardsize/2-midsize/2).coords, (cardsize/2+midsize/2).coords], rounding, (255,255,255))

	d = ImageDraw.Draw(txt := Image.new("L", midsize.coords[::-1], 255))
	d.text((midsize/2).coords[::-1], text, 0, ImageFont.truetype("Ubuntu-M.ttf", 200), "mm")
	img.paste(txt.rotate(90, expand=True, fillcolor=255), ((cardsize-midsize)//2).coords)

	return img