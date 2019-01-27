#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import tensorflow as tf
import sys
import os
import csv

# Disable tensorflow compilation warnings
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

'''
Classify images from test folder and predict slide type
'''

def classify_image(image_path):
    
    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line
                   in tf.gfile.GFile("trained_model/retrained_labels.txt")]

    print (label_lines )

    # Unpersists graph from file
    with tf.gfile.FastGFile("trained_model/retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    files = os.listdir(image_path)
    resultlog = []
    with tf.Session() as sess:
         for file in files:
             # Read the image_data

             if file.endswith('.jpg'): # dirty workaound to filter out the .DSFILE on OSX
                image_data = tf.gfile.FastGFile(image_path+'/'+file, 'rb').read()
                # Feed the image_data as input to the graph and get first prediction
                softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

                predictions = sess.run(softmax_tensor, \
                                       {'DecodeJpeg/contents:0': image_data})

                # Sort to show labels of first prediction in order of confidence
                top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
                records = []
                row_dict = {}
                head, tail = os.path.split(file)
                row_dict['id'] = tail.split('.')[0]

                for node_id in top_k:
                    human_string = label_lines[node_id]
                    score = predictions[0][node_id]
                    #print('%s (score = %.5f)' % (human_string, score))
                    row_dict[human_string] = score
                resultlog.append (row_dict)
                print (row_dict)


def main():
    # CHANGE THIS FOLDER NAME
    test_data_folder = '/Users/Shared/SWD/TENSORFLOW-EXPERIMENTS/PV_SS/TEST/'
    classify_image(test_data_folder)

if __name__ == '__main__':
    main()
