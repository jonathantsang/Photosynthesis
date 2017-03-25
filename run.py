import numpy as np
import os
import PIL.Image
import math

## Run
def scaleImage(dimension):
	## file is a string for the filename\
	i = 0
	factor = 1
	for file in os.listdir("."):
		factor = 1
		if file.endswith(".jpg"):
			img = PIL.Image.open(file)
			width, height = img.size
			smallest = min(width,height)
			factor = int(math.ceil(float(dimension) / float(smallest)))
			## Adjust by the factor to keep aspect ratio
			width *= factor
			height *= factor
			img = img.resize((width, height))
			img = img.crop((0, 0, dimension, dimension))
			img.save("test_" + str(i) + ".png")
			i += 1

scaleImage(256)