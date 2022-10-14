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


from_epoch = 168
to_epoch = 168

dataset_1 = ['Indoor Sequences', 'Outdoor Sequences'] #

dataset2 = {
            'Indoor Sequences':['bootstrap', 'camouflage', 'illumination changes', 'modified background', 'moving camera', 'occlusions', 'simple sequences'],     #, 'simulated motion'             
            'Outdoor Sequences':['cloudy conditions', 'moving camera', 'rainy conditions', 'snowy conditions', 'sunny conditions'],  #, 'simulated motion'  
                
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

            'cloudy conditions':['O_CL_02'],  #, 'O_CL_02'
            'moving camera':['O_MC_02'], #, 'O_MC_02'
            'rainy conditions':['O_RA_02'], #, 'O_RA_02'
            'simulated motion':['O_SM_01', 'O_SM_02', 'O_SM_03', 'O_SM_04', 'O_SM_05', 'O_SM_06', 'O_SM_07', 'O_SM_08', 'O_SM_09', 'O_SM_10', 'O_SM_11', 'O_SM_12'], 
            'snowy conditions':['O_SN_02'], #, 'O_SN_02'
            'sunny conditions':['O_SU_02'],  #, 'O_SU_02'
}

for a in range(from_epoch, to_epoch+1):

    print("Epoch No. --->>> "+str(a).zfill(3))
    for category in dataset_1:   
    
        scene_list = dataset2[category]
       
        for scene in scene_list:
     
            if (category=='Indoor Sequences'):
                part_list = dataset3[scene]
            elif (category=='Outdoor Sequences'):
                part_list = dataset4[scene]
    
            for part in part_list:
                
                dirName = r'C:\Users\santo\OneDrive\Desktop\soumendu_work\lasiesta_results\\'+category+'\\'+scene+'\\'+part+'\predicted\e'+str(a).zfill(3)                                                                                          
    
                if not os.path.exists(dirName):
                    os.mkdir(dirName)
                
                print ('post calculation for ->>> ' + category + ' / ' + scene+ ' / ' + part)
                img_dir = r'C:\Users\santo\OneDrive\Desktop\soumendu_work\lasiesta_results\\'+category+'\\'+scene+'\\'+part+'\pre_prd\e'+str(a).zfill(3)+'\\'
                X_list = glob.glob(os.path.join(img_dir,'*png'))
                x = 0
    			#print(len(X_list))
                for img_add in X_list:
                    x=x+1
                    print("comp->>>"+str(x)+" / "+str(len(X_list)))
    				#post-processing techniques:
                    label = cv2.imread(img_add, 0)	
    				#median or guassian filtering
    				#blur = cv2.medianBlur(label,9)
                    blur = cv2.GaussianBlur(label,(7,7),0)
    				#blur = cv2.bilateralFilter(label,7,25,25)
    				#otsu thresholding
                    ret, label = cv2.threshold(blur,100,255,cv2.THRESH_BINARY)#+cv2.THRESH_OTSU)
    				#filling hol
                    label=ndimage.binary_fill_holes(label).astype(int)
    				#showing
                    label = label.reshape(256,256,1)
                    label = kImage.array_to_img(label)
    
                    label.save(r'C:\Users\santo\OneDrive\Desktop\soumendu_work\lasiesta_results\\'+category+'\\'+scene+'\\'+part+'\predicted\e'+str(a).zfill(3)+'\\'+((os.path.basename(img_add)).split('.')[-2])+'.png')
    












