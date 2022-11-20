#UPDATED 11/19/22
#reduced print lines portion to one line, much more efficient

import cv2 as cv
import time
import numpy as np
import random
from os import system
import math


def main():

	# Darkest values are assigned smaller characters
	# While brighter values are assigned bigger characters

	#16 char long --- remove multiplier of 4 in print line
	# density = ".:^*!%@&#A80HFSB"

	#34 char long --- needs a multiplier of 4 to bring the correcr range for pixels
	density = ".,_><-:+~`^*!?/I%@&#AM0DHFS()[]PB8"
	
	cap = cv.VideoCapture(0, cv.CAP_DSHOW)

	width = 120
	height = 90

	dimension = (width, height)
	# last_time = time.time()
	blank_image = np.zeros(shape=[200, 200, 3], dtype=np.uint8)
	blank_frame = cv.putText(blank_image, 'PRESS Q TO QUIT', (30, 100), cv.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
	cv.imshow('WINDOW', blank_frame)

	while True:
		_, frame = cap.read()

		resized_frame = cv.resize(cv.cvtColor(cv.flip(frame, 1), cv.COLOR_BGR2GRAY), dimension, interpolation=cv.INTER_AREA)

		# clears screen for next frame to display properly
		system('cls')

		# Slight manual crop for window to not stutter by hitting bottom of screen
		for lenPixel in range(23, height-20):
			for widthPixel in range(4, width):
				# brightness_level = math.trunc((resized_frame[lenPixel, widthPixel] / len(density)) * 4)
				# divides pixel brightness by length of the density string and multiplies by 4 to "map" the brightness
				# to a character. Multiplies by 4 to correctly put in range, and allows for greater ranges with higher multiplier
				print(density[math.trunc((resized_frame[lenPixel, widthPixel] / len(density)) * 4)], end='')

			# jumps to nextline for next row of pixels
			print()

		# method to quit program by pressing q into the window
		if cv.waitKey(1) & 0xFF == ord('q'):
			break

	cap.release()
	cv.destroyAllWindows()

main()