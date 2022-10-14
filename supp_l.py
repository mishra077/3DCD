# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:45:01 2019

@author: MEMS_Santosh_WS
"""


import os
import glob
import cv2
from keras.preprocessing import image as kImage

epoch_no = 60
a = epoch_no

dataset_1 = ['Outdoor Sequences'] #, 'Outdoor Sequences'

dataset2 = {
            'Indoor Sequences':['bootstrap'],     #, 'simulated motion'             
            'Outdoor Sequences':['sunny conditions'],  #, 'simulated motion'  
                
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



folder = r'C:\Users\santo\OneDrive\Desktop\soumendu_work\LASIESTA'
folder2 = r'C:\Users\santo\OneDrive\Desktop\soumendu_work\lasiesta_results'
x = 0
y = 0
v=0
w=0
for category in dataset_1:   

    scene_list = dataset2[category]
   
    for scene in scene_list:
       
 
        if (category=='Indoor Sequences'):
            part_list = dataset3[scene]
        elif (category=='Outdoor Sequences'):
            part_list = dataset4[scene]

        for part in part_list:
            print('Supp calculation for ->>> ' + category + ' / ' + scene + ' / ' + part)
            image_path_list = glob.glob(os.path.join(folder+'\\'+category+'\\'+scene+'\\'+part+'\col_256\\'+'*bmp'))
            image_path_list = sorted(image_path_list)
            #print(image_path_list[1])
            label_path_list = glob.glob(os.path.join(folder2+"\\"+category+"\\"+scene+"\\"+part+"\predicted\e"+str(a).zfill(3)+"\\"+"*png"))
            label_path_list = sorted(label_path_list)
            #print(label_path_list[1])
            h=0
            for i,(image_path, label_path) in enumerate(zip(image_path_list[49:],label_path_list)):
                print('comp no. ->>> '+str(h+1)+' / '+str(len(label_path_list)))
                h=h+1
                #rgbArray = np.zeros((256,256,3), 'uint8')
                img = cv2.imread(image_path)
                img = kImage.img_to_array(img)
                lbl = cv2.imread(label_path, 0)
                lbl = kImage.img_to_array(lbl)
                b = ((os.path.basename(image_path)).split('-')[-1]).split('.')[-2]
                #b = ((os.path.basename(label_path)).split('-GT_')[-1]).split('.')[-2]
                
                img = img.reshape(256,256,3)
                lbl = lbl.reshape(256,256)
                #lbl = kImage.array_to_img(lbl)
                
                for n in range(256):
                    for k in range(256):
                        if(lbl[n][k]==0):
                            img[n][k][0]=0
                            img[n][k][1]=0
                            img[n][k][2]=0
                            
                img = img.reshape(3,256,256)
                img = kImage.array_to_img(img)
                img.save(folder2+'\\'+category+'\\'+scene+'\\'+part+'\supp\\'+((os.path.basename(image_path)).split('-')[-2])+'-'+b.zfill(6)+'.bmp')
                #lbl.save(folder+'\\'+category+'\\'+scene+'\\'+part+'\gt_256\\'+((os.path.basename(label_path)).split('-GT_')[-2])+'-GT_'+b.zfill(6)+'.png')
                #print(folder+'\\'+category+'\\'+scene+'\\'+part+'\gt_256\\'+((os.path.basename(label_path)).split('-GT_')[-2])+'-GT_'+str(b).zfill(6)+'.png')
                
           
		
         