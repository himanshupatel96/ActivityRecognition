# -*- coding: utf-8 -*-

import cv2
import numpy as np
import sys, os, random
import signal, time, math

# This script reads videos 1.avi through 600.avi at the rate of 30 frames/sec and converts them into a bunch of image files.
# Each image is a single frame from the video.

save_directory = '../ActivityRecognitionDataSet/'

def load_fragment_store(load_path, store_path, total_videos):

	vid = 1
	div = int(math.ceil(len(total_videos)/50.0))
	for video in total_videos:

		video_path = load_path+str(video)+'.avi'
		cap = cv2.VideoCapture(video_path)
		
		# Wait unitl video is loaded
		while not cap.isOpened():
			cap = cv2.VideoCapture(video_path)
			cv2.waitKey(100)

		pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
		image = 1
		while True:
			flag, frame = cap.read()
			if flag:
				cv2.imwrite(store_path+str(vid)+'-'+str(image)+'.png', frame)
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

		progress = ('█'*(vid/div))+(' '*((len(total_videos) - vid)/div))
		sys.stdout.write("\rVideo Processing in progress: %s | %.2f %s"%(progress, (vid*100.0)/len(total_videos), '%'))
		sys.stdout.flush()
		vid += 1

	print '\n Processed!'

# Specifying load paths
fight_video_load_path = '../ML/fight/'
noFight_video_load_path = '../ML/noFight/'

# Specifying store paths
fight_video_train_save_path 	= save_directory + 'train/fight/'
fight_video_test_save_path 		= save_directory + 'test/fight/'
noFight_video_train_save_path 	= save_directory + 'train/noFight/'
noFight_video_test_save_path	= save_directory + 'test/noFight/'

# Specifying no of videos and randomizing them
input_size = 600
input_range = range(1,input_size)
random.shuffle(input_range)

# Doing the real stuff
load_fragment_store(fight_video_load_path, fight_video_test_save_path, input_range[input_size-50:])
load_fragment_store(fight_video_load_path, fight_video_train_save_path, input_range[:input_size-50])
load_fragment_store(fight_video_load_path, noFight_video_test_save_path, input_range[input_size-50:])
load_fragment_store(fight_video_load_path, noFight_video_train_save_path, input_range[:input_size-50])