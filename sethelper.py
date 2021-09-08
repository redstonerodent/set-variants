from PIL import Image, ImageDraw, ImageFont

cardsize = cardwidth, cardheight = 825, 1125 # poker deck on thegamecrafter.com


def setback(text, color):
	midw, midh = 201, 501 # should be odd
	rounding = 50
	draw = ImageDraw.Draw(img := Image.new("RGB", cardsize, color))

	draw.rounded_rectangle([cardwidth/2-midw/2, cardheight/2-midh/2, cardwidth/2+midw/2, cardheight/2+midh/2], rounding, (255,255,255))

	d = ImageDraw.Draw(txt := Image.new("L", [midh, midw], 255))
	d.text([midh/2, midw/2], text, 0, ImageFont.truetype("Ubuntu-M.ttf", 200), "mm")
	img.paste(txt.rotate(90, expand=True, fillcolor=255), [(cardwidth-midw)//2, (cardheight-midh)//2])

	return img