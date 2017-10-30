# -*- coding: utf-8 -*-

import cv2
import numpy as np
import sys, os
import signal, time

# This script reads videos 1.avi through 600.avi at the rate of 30 frames/sec and converts them into a bunch of image files.
# Each image is a single frame from the video.

video = 1
image = 1
total_videos = 600
save_path = '../ActivityRecognitionDataSet/'

while video <= total_videos:

	video_path = '../ML/fights/'+str(video)+'.avi'
	cap = cv2.VideoCapture(video_path)
	
	# Wait unitl video is loaded
	while not cap.isOpened():
		cap = cv2.VideoCapture(video_path)
		cv2.waitKey(100)

	pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
	while True:
		flag, frame = cap.read()
		if flag:
			cv2.imwrite(save_path+str(image)+'.png', frame)
			image += 1
			pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)

		else:
			# Next frame is not yet ready, so we wait for 1 second
			cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, pos_frame - 1)
			cv2.waitKey(1000)

		if cv2.waitKey(10) == 27:
			break

		if cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES) == cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT):
			# If all the frames are read, then end the loop
			break

	progress = ('█'*(video/12))+(' '*((total_videos - video)/12))
	sys.stdout.write("\rVideo Processing in progress: %s | %.2f %s"%(progress, (video*100.0)/total_videos, '%'))
	sys.stdout.flush()
	video += 1

print '\nVideos Processed!'