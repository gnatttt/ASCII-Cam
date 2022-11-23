import cv2 as cv
import time
import numpy as np
import random
from os import system
import math
import subprocess


def WebcamToAscii():

	# Darkest values are assigned smaller characters
	# While brighter values are assigned bigger characters

	#16 char long --- remove multiplier of 4 in print line
	# density = ".:^*!%@&#A80HFSB"

	#34 char long --- needs a multiplier of 4 to bring the correct range for pixels
	# density = ".,_><-:+~`^*!?/I%@&#AM0DHFS()[]PB8"

	density = ' .\'`^",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
	
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
		for lenPixel in range(18, height-20):
			for widthPixel in range(4, width):
				# brightness_level = math.trunc((resized_frame[lenPixel, widthPixel] / len(density)) * 4)
				# divides pixel brightness by length of the density string and multiplies by 4 to "map" the brightness
				# to a character. Multiplies by 4 to correctly put in range, and allows for greater ranges with higher multiplier
				print(density[math.trunc((resized_frame[lenPixel, widthPixel] / len(density)) * 18.9)], end='')

			# jumps to nextline for next row of pixels
			print()

		# method to quit program by pressing q into the window
		if cv.waitKey(1) & 0xFF == ord('q'):
			break

	cap.release()
	cv.destroyAllWindows()

def ImageToAscii(file):
	# This sequence is used for white backgrounds
	density = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'. '

	# This sequence is used for black backgrounds
	# density = ' .\'`^",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
	img = cv.imread(file, 0)
	SCREEN_RESO = 300
	height, width = img.shape

	scale_percent = round(((width - SCREEN_RESO) / width), 1)

	height = int(height - height * scale_percent)
	width = int(width - width * scale_percent)
	dimension = (width, height)

	resized_img = cv.resize(img, dimension, interpolation = cv.INTER_AREA)

	print("WRITING TO FILE...")

	file = open("output.txt", "w")
	for lenPixel in range(height):
		for widthPixel in range(width):
			# brightness_level = math.trunc((resized_frame[lenPixel, widthPixel] / len(density)) * 4)
			# divides pixel brightness by length of the density string and multiplies by 4 to "map" the brightness
			# to a character. Multiplies by 4 to correctly put in range, and allows for greater ranges with higher multiplier
			file.write(density[math.trunc((resized_img[lenPixel, widthPixel] / len(density)) * 18.9)])

		# jumps to nextline for next row of pixels
		file.write("\n")
	file.close()
	print("COMPLETED\n")
	print("----		File name >> output.txt")
	print("----		Open with Notepad")
	print("----		Change font to Consolas at regular")
	print("----		Zoom out if needed\n")


def main():
	print("(1) ---- WEBCAM TO ASCII")
	print("(2) ---- IMAGE TO ASCII")
	choice = input("> ")

	if choice == "1":
		print("TURNING ON WEBCAM")
		time.sleep(2)
		WebcamToAscii()

	elif choice == "2":
		print("--ENTER FILE NAME--")
		file = input("> ")

		ImageToAscii(file)
		launch = input("Open ascii file?: ")
		if launch == "yes":
			print("**** MAKE SURE TO ZOOM OUT ****")
			system("output.txt")

		print("PROCESS COMPLETED")
main()