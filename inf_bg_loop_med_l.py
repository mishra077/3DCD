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


from_epoch = 84
to_epoch = 84

config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.3
set_session(tf.Session(config=config))


    
#dataset_1 = ['Indoor Sequences', 'Outdoor Sequences'] #
dataset_1 = ['Outdoor Sequences'] #
#dataset2 = {
#            'Indoor Sequences':['bootstrap', 'camouflage', 'illumination changes', 'modified background', 'moving camera', 'occlusions', 'simple sequences'],     #, 'simulated motion'             
#            'Outdoor Sequences':['cloudy conditions', 'moving camera', 'rainy conditions', 'snowy conditions', 'sunny conditions'],  #, 'simulated motion'  
#                
#}
dataset2 = {
            'Outdoor Sequences':['moving camera', 'rainy conditions'],  #, 'simulated motion', 'snowy conditions'
                
}

dataset3 = {
            'bootstrap':['I_BS_02'],   #, 'I_BS_02'
	        'camouflage':['I_CA_02'],   #, 'I_CA_02'
            'illumination changes':['I_IL_02'],   #, 'I_IL_02'
	        'modified background':['I_MB_02'],   #, 'I_MB_02'
            'moving camera':['I_MC_02'],   #, 'I_MC_02'
            'occlusions':['I_OC_02'],   #, 'I_OC_02'
            'simple sequences':['I_SI_02'],   #, 'I_SI_02'
            'simulated motion':['I_SM_01', 'I_SM_02', 'I_SM_03', 'I_SM_04', 'I_SM_05', 'I_SM_06', 'I_SM_07', 'I_SM_08', 'I_SM_09', 'I_SM_10', 'I_SM_11', 'I_SM_12'],   
}
dataset4 = {               

            #'cloudy conditions':['O_CL_01'],  #, 'O_CL_02'
            'moving camera':['O_MC_02'], #, 'O_MC_02'
            #'rainy conditions':['O_RA_01'] #, 'O_RA_02'
            #'simulated motion':['O_SM_01', 'O_SM_02', 'O_SM_03', 'O_SM_04', 'O_SM_05', 'O_SM_06', 'O_SM_07', 'O_SM_08', 'O_SM_09', 'O_SM_10', 'O_SM_11', 'O_SM_12'], 
            #'snowy conditions':['O_SN_02', 'O_SN_01'], #, 'O_SN_02'
            #'sunny conditions':['O_SU_02'],  #, 'O_SU_02'
}
void_label = 0
folder= r'C:\Users\santo\OneDrive\Desktop\soumendu_work\LASIESTA'

for a in range(from_epoch, to_epoch+1):

    model_path = r'C:\Users\santo\OneDrive\Desktop\soumendu_work\bgs3\2dcd_median models\complete_SD\dsfmdl.'+str(a).zfill(3)+'.h5'
    model = load_model(model_path) 
    print("Model Loaded --->>> "+str(a).zfill(3))

    X = np.zeros((1,50, 256, 256), dtype='float32')
    main_X = np.zeros((1, 1, 256, 256), dtype='float32')
    M = np.zeros((1, 1, 256, 256), dtype='float32')

    

    for category in dataset_1:   
    
        scene_list = dataset2[category]
       
        for scene in scene_list:
     
            if (category=='Indoor Sequences'):
                part_list = dataset3[scene]
            elif (category=='Outdoor Sequences'):
                part_list = dataset4[scene]
    
            for part in part_list:
    
                dirName = r'C:\Users\santo\OneDrive\Desktop\soumendu_work\lasiesta_results\\'+category+'\\'+scene+'\\'+part+'\pre_prd\e'+str(a).zfill(3)                                                                                          
    
                if not os.path.exists(dirName):
                    os.makedirs(dirName)
    
                print('Output calculation for ->>> ' + category + ' / ' + scene + ' / ' + part)
                image_path_list = glob.glob(os.path.join(folder+'\\'+category+'\\'+scene+'\\'+part+'\in_256\\'+'*bmp'))
                image_path_list = sorted(image_path_list)
                label_path_list = glob.glob(os.path.join(folder+'\\'+category+'\\'+scene+'\\'+part+'\gt_256\\'+'*png'))
                label_path_list = sorted(label_path_list)
                median_path_list = glob.glob(os.path.join(folder+'\\'+category+'\\'+scene+'\\'+part+'\median\\'+'*png'))
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
                        main_img = main_img.reshape(256, 256)
                        main_X[0][0] = main_img
                        med_img = cv2.imread(median_path, 0)
                        med_img = KImage.img_to_array(med_img)
                        med_img = med_img.reshape(-1)
                    if (len(idx)>0):
                        med_img[idx] = void_label
                        med_img = med_img.reshape(256, 256)
                        M[0][0] = med_img
                    for x in range(50):
                        image = cv2.imread(image_path_list[49+i-x], 0)
                        image = KImage.img_to_array(image)
                        image = image.reshape(-1)
                        if (len(idx)>0):
                            image[idx] = void_label
                            image = image.reshape(256, 256)
                            X[0][x] = image
                    label = model.predict( [X, M, main_X], batch_size=None, verbose=1, steps=None)
                    #label = np.floor(label)
                    label = label.reshape(256,256,1)
                            
                    label *=255
                    label = kImage.array_to_img(label)
                    label.save(r'C:\Users\santo\OneDrive\Desktop\soumendu_work\lasiesta_results\\'+category+'\\'+scene+'\\'+part+'\pre_prd\e'+str(a).zfill(3)+'\\bin'+((os.path.basename(image_path)).split('.')[-2]).split('in')[-1]+'.png')
                            