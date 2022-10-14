# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 16:33:43 2019

@author: MEMS_Santosh_WS
"""

import numpy as np
import random as rn
import os
import os
import json
import pickle
import gc

import numpy as np
import cv2

from PIL import Image
#from extra import PolyDecay
#from extra import OurGenerator
import glob
from keras.preprocessing import image as kImage




#change



from random import shuffle
import numpy as np
import cv2
from keras.preprocessing import image as KImage
from keras.callbacks import Callback
from keras.layers import concatenate
from keras.layers.core import Lambda
from keras.models import Model
from keras.utils.data_utils import Sequence
from keras import backend as K
from scipy import ndimage



epochs = [25, 30, 37, 40, 45, 50]

dataset_1 = ['shadow']

dataset = {
            'badWeather':['wetSnow', 'skating', 'snowFall','blizzard'],                                                             #, 'wetSnow'blizzard
            'baseline':['highway', 'pedestrians', 'PETS2006','office'],                                                            #, 'office'
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



for a in epochs:

      print("For epoch no. --->>> "+str(a).zfill(3))

      for category in dataset_1:   

            scene_list = dataset[category]

            for scene in scene_list:

                  dirName = r'C:\Users\santo\OneDrive\Desktop\soumendu_work\3D-Medical-Segmentation-GAN-master\Results_50p\Results_50p_v2\g_2'+'\\'+category+'\\'+scene+'\\predicted_loop\\e'+str(a).zfill(3)+'\Cd'                                                                                           

                  if not os.path.exists(dirName):
                      os.makedirs(dirName)
                      
                  print ('post calculation for ->>> ' + category + ' \\ ' + scene)
                  img_dir = r'C:\Users\santo\OneDrive\Desktop\soumendu_work\3D-Medical-Segmentation-GAN-master\Results_50p\Results_50p_v2\g_2'+'\\'+category+'\\'+scene+'\\pre_prd_loop\\e'+str(a).zfill(3)+'\Cd\\' 
                  X_list = glob.glob(os.path.join(img_dir,'*png'))
                  x = 0
                  for img_add in X_list:
                      x=x+1
                      print("comp->>>"+str(x)+" \\ "+str(len(X_list)))
                      #post-processing techniques:
                      label = cv2.imread(img_add, 0)  
                      #median or guassian filtering
                      #blur = cv2.medianBlur(label,9)
                      blur = cv2.GaussianBlur(label,(5,5),0)
                      #blur = cv2.bilateralFilter(label,7,25,25)
                      #otsu thresholding
                      ret, label = cv2.threshold(blur,155,255,cv2.THRESH_BINARY)#+cv2.THRESH_OTSU)
                      #filling hol
                      label=ndimage.binary_fill_holes(label).astype(int)
                      #showing
                      label = label.reshape(256,256,1)
                      label = kImage.array_to_img(label)
                      
                      label.save(r'C:\Users\santo\OneDrive\Desktop\soumendu_work\3D-Medical-Segmentation-GAN-master\Results_50p\Results_50p_v2\g_2'+'\\'+category+'\\'+scene+'\\predicted_loop\\e'+str(a).zfill(3)+'\Cd\\post'+((os.path.basename(img_add)).split('.')[-2]).split('bin')[-1]+'.png')












