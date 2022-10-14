# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 18:00:13 2019

@author: MEMS_Santosh_WS
"""


import numpy as np
import tensorflow as tf
import random as rn
import os
import os
import json
import pickle
import gc

import numpy as np
import cv2
from keras import optimizers
from keras.callbacks import ModelCheckpoint
from keras.callbacks import TensorBoard
from keras.callbacks import LearningRateScheduler
from keras.utils import multi_gpu_model
from keras.models import load_model
from keras import backend as K
import tensorflow as tf
from PIL import Image
#from extra import PolyDecay
#from extra import OurGenerator
import glob
from keras.preprocessing import image as kImage

#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'




#change



from random import shuffle
import numpy as np
import cv2

from keras.utils import to_categorical
from keras.preprocessing import image as KImage
from keras.callbacks import Callback
from keras.layers import concatenate
from keras.layers.core import Lambda
from keras.models import Model
from keras.utils.data_utils import Sequence
from keras import backend as K
from scipy import ndimage
from keras.backend.tensorflow_backend import set_session


from_epoch = 110
to_epoch = 120

config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.3
set_session(tf.Session(config=config))


    
dataset_1 = ['baseline']

dataset = {
            'badWeather':['wetSnow', 'skating', 'snowFall','blizzard'],                                                             #, 'wetSnow'blizzard
            'baseline':['pedestrians'],#['highway', 'pedestrians', 'PETS2006','office'],                                                            #, 'office'
            'cameraJitter':['badminton', 'sidewalk', 'traffic','boulevard'],                                                          #, 'boulevard'
            'dynamicBackground':['fountain02', 'canoe', 'fall', 'fountain01', 'overpass','boats'],                                     #, 'boats'
            'intermittentObjectMotion':['abandonedBox', 'sofa', 'parking', 'tramstop', 'winterDriveway','streetLight'],             #, ''streetLight
            'lowFramerate':['port_0_17fps', 'tramCrossroad_1fps', 'tunnelExit_0_35fps','turnpike_0_5fps'],                                  #, 'turnpike_0_5fps'
            'nightVideos':['bridgeEntry','busyBoulvard','fluidHighway','streetCornerAtNight', 'winterStreet','tramStation'],            #,'tramStation'
            #'PTZ':['continuousPan', 'intermittentPan', 'twoPositionPTZCam', 'zoomInZoomOut'],
            'shadow':['backdoor', 'bungalows', 'copyMachine', 'cubicle', 'peopleInShade','busStation'],                                #, 'busStation'
            'thermal':['lakeSide', 'diningRoom', 'library', 'park','corridor'],                                                      #, ''corridor
            'turbulence':['turbulence0', 'turbulence2', 'turbulence3','turbulence1']                                                   #, 'turbulence1'
}

void_label = 0
folder=r'C:\Users\santo\OneDrive\Desktop\soumendu_work\dataset2014'

for a in range(from_epoch, to_epoch+1):

    model_path = r'C:\Users\santo\OneDrive\Desktop\soumendu_work\data\model_save\3dcd_catwise_murari\baseline\leave_pedestrian_out\no_cmf\dsfmdl.'+str(a).zfill(3)+'.h5'
    model = load_model(model_path) 
    print("Model Loaded --->>> "+str(a).zfill(3))

    X = np.zeros((1,50, 256, 256, 1), dtype='float32')
    main_X = np.zeros((1, 1, 256, 256, 1), dtype='float32')
    M = np.zeros((1, 1, 256, 256, 1), dtype='float32')

    

    for category in dataset_1:   

        scene_list = dataset[category]


        for scene in scene_list:

            dirName = r'D:\soumendu_data\2dcd_median_result'+'\\'+category+'\\'+scene+'\\pre_prd_loop2\\e'+str(a).zfill(3)                                                                                          

            if not os.path.exists(dirName):
                #os.mkdir( r'C:\Users\santo\OneDrive\Desktop\soumendu_work\results_all_2dcd_median'+'\\'+category)
                #os.mkdir( r'C:\Users\santo\OneDrive\Desktop\soumendu_work\results_all_2dcd_median'+'\\'+category+'\\'+scene)
                #os.mkdir( r'C:\Users\santo\OneDrive\Desktop\soumendu_work\results_all_2dcd_median'+'\\'+category+'\\'+scene+'\\pre_prd_loop')
                os.mkdir(dirName)

            print('Output calculation for ->>> ' + category + ' \\ ' + scene)
            image_path_list = glob.glob(os.path.join(folder+'\\'+category+'\\'+scene+'\\input\\'+'*jpg'))
            image_path_list = sorted(image_path_list)
            label_path_list = glob.glob(os.path.join(folder+'\\'+category+'\\'+scene+'\\groundtruth\\'+'*png'))
            label_path_list = sorted(label_path_list)
            median_path_list = glob.glob(os.path.join(folder+'\\'+category+'\\'+scene+'\\median\\'+'*png'))
            median_path_list = sorted(median_path_list)

            for i,(image_path, label_path, median_path) in enumerate(zip(image_path_list[49:],label_path_list[49:],median_path_list)):

                label_ac = cv2.imread(label_path, 0)
                label_ac = KImage.img_to_array(label_ac)
                label_ac /= 255.0
                label_ac = label_ac.reshape(-1)
                idx = np.where(np.logical_and(label_ac>0.25, label_ac<0.8))[0] # find non-ROI
                #label_ac = label_ac.reshape(256, 256)
                main_img = cv2.imread(image_path, 0)
                main_img = KImage.img_to_array(main_img)
                main_img = main_img.reshape(-1)
                if (len(idx)>0):
                    main_img[idx] = void_label
                main_img = main_img.reshape(256, 256, 1)
                main_X[0][0] = main_img
                
                med_img = cv2.imread(median_path, 0)
                med_img = KImage.img_to_array(med_img)
                med_img = med_img.reshape(-1)
                if (len(idx)>0):
                    med_img[idx] = void_label
                med_img = med_img.reshape(256, 256, 1)
                M[0][0] = med_img
                
                for x in range(50):

                    image = cv2.imread(image_path_list[49+i-x], 0)
                    image = KImage.img_to_array(image)
                    image = image.reshape(-1)
                    if (len(idx)>0):
                        image[idx] = void_label
                    image = image.reshape(256, 256, 1)
                    X[0][x] = image
                label = model.predict( [X, main_X], batch_size=None, verbose=1, steps=None)
                #label = np.floor(label)
                label = label.reshape(256,256,1)

                label *=255
                label = kImage.array_to_img(label)
                label.save(r'D:\soumendu_data\2dcd_median_result\\'+category+'\\'+scene+'\\pre_prd_loop2\\e'+str(a).zfill(3)+'\\bin'+((os.path.basename(image_path)).split('.')[-2]).split('in')[-1]+'.png')


