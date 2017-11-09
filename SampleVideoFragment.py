# -*- coding: utf-8 -*-

import cv2
import numpy as np
import sys, os, random
import signal, time, math

# This script reads videos 1.avi through 600.avi at the rate of 30 frames/sec and converts them into a bunch of image files.
# Each image is a single frame from the video.

save_directory = '../ActivityRecognitionDataSet/'

def load_fragment_store(load_path, store_path):

	sec = 1

	cap = cv2.VideoCapture(load_path)
	
	# Wait unitl video is loaded
	while not cap.isOpened():
		cap = cv2.VideoCapture(video_path)
		cv2.waitKey(100)

	pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
	image = 1
	while True:
		flag, frame = cap.read()
		if flag:
			cv2.imwrite(store_path+str(sec)+'-'+str(image)+'.jpeg', frame)
			# cv2.imshow('Video', frame)
			image += 1
			if image > 50:
				print 'Second '+str(sec)+' processed'
				image, sec = 0, sec+1
			if sec > 60:
				break
			pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
			# print time.ctime(), pos_frame

		else:
			# Next frame is not yet ready, so we wait for 1 second
			cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, pos_frame - 1)
			cv2.waitKey(1000)

		if cv2.waitKey(10) == 27:
			break

		if cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES) == cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT):
			# If all the frames are read, then end the loop
			break
		# if cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES) >= 300:
		# 	# If all the frames are read, then end the loop
		# 	break

	print '\n Processed!'

# Classes
classes = ['biking', 'fighting', 'hand_action', 'running']

# Specifying load path
load_path = '../ML/sample_fight.mp4'

# Specifying store path
save_path = save_directory + 'sample/fighting/'

# Doing the real stuff
load_fragment_store(load_path, save_path)