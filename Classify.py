import tensorflow as tf 
import sys
import operator

label_lines = [line.rstrip() for line in tf.gfile.GFile("../tensorflow/~/ActivityRecognition/retrained_labels.txt")]
classes = ['biking', 'fighting', 'hand_action', 'running']

with tf.gfile.FastGFile("../tensorflow/~/ActivityRecognition/retrained_graph.pb", "rb") as f:
	graph_def = tf.GraphDef()
	graph_def.ParseFromString(f.read())
	_ = tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
	softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

	pred = []

	for j in range(1,60):
		freq = {}

		for i in range(1,51):
			# image_path = "../ActivityRecognitionDataSet/test/%s/%d-%d.jpeg"%(cls, j,i)
			image_path = "../ActivityRecognitionDataSet/sample/fighting/%d-%d.jpeg"%(j,i)
			try:
				image_data = tf.gfile.FastGFile(image_path, 'rb').read()
			except:
				break

			predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})

			top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

			# for node_id in top_k:
			human_string = label_lines[top_k[0]]
			# score = predictions[0][node_id]
				# print("%s (%.5f)"%(human_string, score))
			freq[human_string] = freq.get(human_string, 1) + 1
		print(sorted(freq.items(), key=operator.itemgetter(1), reverse=True)[0][0])
	# print(cls, ' : ',pred)
