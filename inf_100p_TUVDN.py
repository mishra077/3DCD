
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
import glob
from keras.preprocessing import image as kImage
from keras.models import model_from_json

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

os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID";
 
os.environ["CUDA_VISIBLE_DEVICES"]="0";  


from_epochs = 20
to_epochs = 51


config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.9
set_session(tf.Session(config=config))


    
dataset_1 = ['Dust', 'Fog', 'Low Light', 'Rain'] #

dataset2 = {
            'Dust':['Dynamic Background', 'Flat Cluttered Background'],     #             
            'Fog':['Dynamic Background', 'Flat Cluttered Background'], 
            'Low Light':['Dynamic Background', 'Flat Cluttered Background'],     #             
            'Rain':['Dynamic Background', 'Flat Cluttered Background'], #  
                
}

dataset3 = {
            'Dynamic Background':['D12_DB_14082018', 'D13_DB_14082018'],   #, 'I_BS_02'
            'Flat Cluttered Background':['D2_FCB_06072018', 'D6_FCB_14082018']
}
dataset4 = {
            'Dynamic Background':['F8_DB_20012019', 'F9_DB_20012019'],   #, 'I_BS_02'
            'Flat Cluttered Background':['F1_FCB_26122018', 'F5_FCB_20012019']
}
dataset5 = {
            'Dynamic Background':['LL15_DB_03082018', 'LL19_DB_19062019'],   #, 'I_BS_02'
            'Flat Cluttered Background':['LL8_FCB_06072018', 'LL11_FCB_19062019']
}
dataset6 = {               

            'Dynamic Background':['R4_DB_04092018', 'R5_DB_13072019'],   #, 'I_BS_02'
            'Flat Cluttered Background':['R1_FCB_04092018', 'R3_FCB_13072019']
}

void_label = 0
folder= '/home/users/student21/projectMNIT/data/TU-VDN'
#folder2 = '/home/users/student21/projectMNIT/data/Results_50p_v1/g1'

for a in range(from_epochs, to_epochs):


    with open('/home/users/student21/projectMNIT/data/seq_gan_100p_TUVDN/g_1/e'+str(a).zfill(3)+'/model.json', 'r') as model_file:
        model1 = model_file.read()
    model1 = model_from_json(model1)
    # Getting weights
    model1.load_weights("/home/users/student21/projectMNIT/data/seq_gan_100p_TUVDN/g_1/e"+str(a).zfill(3)+"/weights.h5")
    
    with open('/home/users/student21/projectMNIT/data/seq_gan_100p_TUVDN/g_2/e'+str(a).zfill(3)+'/model.json', 'r') as model_file:
        model2 = model_file.read()
    model2 = model_from_json(model2)
    # Getting weights
    model2.load_weights("/home/users/student21/projectMNIT/data/seq_gan_100p_TUVDN/g_2/e"+str(a).zfill(3)+"/weights.h5")
    
    print("Model Loaded --->>> "+str(a).zfill(3))

    X = np.zeros((1,50, 256, 256, 1), dtype='float32')
    main_X = np.zeros((1, 1, 256, 256, 1), dtype='float32')
    #Bg = np.zeros((1,1, 256, 256, 1), dtype='float32')

    

    for category in dataset_1:   

        scene_list = dataset2[category]


        for scene in scene_list:
 
                if (category=='Dust'):
                    part_list = dataset3[scene]
                elif (category=='Fog'):
                    part_list = dataset4[scene]
                elif (category=='Low Light'):
                    part_list = dataset5[scene]
                elif (category=='Rain'):
                    part_list = dataset6[scene]
                
                
                for part in part_list:

                    dirName_bg = '/home/users/student21/projectMNIT/data/Results_100p_TUVDN/g_1'+'/'+category+'/'+scene+'/'+part+'/pre_prd_loop/e'+str(a).zfill(3)+'/Bg/'
                    dirName_cd = '/home/users/student21/projectMNIT/data/Results_100p_TUVDN/g_2'+'/'+category+'/'+scene+'/'+part+'/pre_prd_loop/e'+str(a).zfill(3)+'/Cd/'

                    if not os.path.exists(dirName_bg):
                        os.makeirs(dirName_bg)

                    if not os.path.exists(dirName_cd):
                        os.makeirs(dirName_cd)

                    print('Output calculation for ->>> ' + category + ' / ' + scene + ' / ' + part)
                    image_path_list = glob.glob(os.path.join(folder+'/'+category+'/'+scene+ '/'+part+'_in_256/'+'*bmp'))
                    image_path_list = sorted(image_path_list)
                    label_path_list = glob.glob(os.path.join(folder+'/'+category+'/'+scene+'/'+part+ '_GT_gt_256/'+'*bmp'))
                    label_path_list = sorted(label_path_list)
                    #mode_path = os.path.join(folder2+'/'+category+'/'+scene+'/pre_prd_loop/e'+str(a).zfill(3)+'*png')

                    for i, label_path in enumerate(label_path_list[4:]):

                        label_ac = cv2.imread(label_path, 0)
                        label_ac = KImage.img_to_array(label_ac)
                        label_ac /= 255.0
                        label_ac = label_ac.reshape(-1)
                        #idx = np.where(np.logical_and(label_ac>0.25, label_ac<0.8))[0] # find non-ROI

                        main_img = cv2.imread(image_path_list[49+(i*10)], 0)
                        main_img = KImage.img_to_array(main_img)
                        main_img = main_img.reshape(-1)
                        #if (len(idx)>0):
                            #main_img[idx] = void_label
                        main_img = main_img.reshape(256, 256, 1)
                        main_X[0][0] = main_img
                        """
                        bckgd = cv2.imread(mode_path, 0)
                        bckgd = KImage.img_to_array(bckgd)
                        #bckgd = bckgd.reshape(-1)
                        #if (len(idx)>0):
                        #    bckgd[idx] = void_label
                        bckgd = bckgd.reshape(256, 256, 1)
                        Bg[0][0] = bckgd
                        """
                        for x in range(50):

                            image = cv2.imread(image_path_list[49+(i*10)-x], 0)
                            image = KImage.img_to_array(image)
                            #image = image.reshape(-1)
                            #if (len(idx)>0):
                            #    image[idx] = void_label
                            image = image.reshape(256, 256, 1)
                            X[0][x] = image
                        
                        label1 = model1.predict(X, batch_size=None, verbose=1, steps=None)
                        label2 = model2.predict( [main_X, label1], batch_size=None, verbose=1, steps=None)
                        #label = np.floor(label)
                        label1 = label1.reshape(256,256,1)
                        label2 = label2.reshape(256,256,1)

                        label2 *=255
                        label1 = kImage.array_to_img(label1)
                        label2 = kImage.array_to_img(label2)
                        label1.save('/home/users/student21/projectMNIT/data/Results_100p_TUVDN/g_1/'+category+'/'+scene+'/'+ part+'/pre_prd_loop/e'+str(a).zfill(3)+'/Bg/back'+((os.path.basename(image_path_list[49+(i*10)])).split('.')[-2]).split('_')[-1]+'.bmp')
                        label2.save('/home/users/student21/projectMNIT/data/Results_100p_TUVDN/g_2/'+category+'/'+scene+'/'+ part+'/pre_prd_loop/e'+str(a).zfill(3)+'/Cd/bin'+((os.path.basename(image_path_list[49+(i*10)])).split('.')[-2]).split('_')[-1]+'.bmp')