import os
import glob


dataset_1 = ['Indoor Sequences', 'Outdoor Sequences'] #

dataset2 = {
            'Indoor Sequences':['bootstrap', 'camouflage', 'illumination changes', 'modified background', 'moving camera', 'occlusions', 'simple sequences'],     #             
            'Outdoor Sequences':['cloudy conditions', 'moving camera', 'rainy conditions', 'snowy conditions', 'sunny conditions'],  #  
                
}
"""
dataset3 = {
            'bootstrap':['I_BS_01'],   #, 'I_BS_02'
	        'camouflage':['I_CA_01'],   #, 'I_CA_02'
            'illumination changes':['I_IL_01'],   #, 'I_IL_02'
	        'modified background':['I_MB_01'],   #, 'I_MB_02'
            'moving camera':['I_MC_01'],   #, 'I_MC_02'
            'occlusions':['I_OC_01'],   #, 'I_OC_02'
            'simple sequences':['I_SI_01'],   #, 'I_SI_02'
            'simulated motion':['I_SM_01', 'I_SM_02', 'I_SM_03', 'I_SM_04', 'I_SM_05', 'I_SM_06', 'I_SM_07', 'I_SM_08', 'I_SM_09', 'I_SM_10', 'I_SM_11', 'I_SM_12'],   
}
dataset4 = {               

            'cloudy conditions':['O_CL_01'],  #, 'O_CL_02'
            'moving camera':['O_MC_01'], #, 'O_MC_02'
            'rainy conditions':['O_RA_01'], #, 'O_RA_02'
            'simulated motion':['O_SM_01', 'O_SM_02', 'O_SM_03', 'O_SM_04', 'O_SM_05', 'O_SM_06', 'O_SM_07', 'O_SM_08', 'O_SM_09', 'O_SM_10', 'O_SM_11', 'O_SM_12'], 
            'snowy conditions':['O_SN_01'], #, 'O_SN_02'
            'sunny conditions':['O_SU_01'],  #, 'O_SU_02'
}
"""

dataset3 = {
            'bootstrap':['I_BS_01', 'I_BS_02'],   #, 'I_BS_02'
            'camouflage':['I_CA_01', 'I_CA_02'],   #, 'I_CA_02'
            'illumination changes':['I_IL_01', 'I_IL_02'],   #, 'I_IL_02'
            'modified background':['I_MB_01', 'I_MB_02'],   #, 'I_MB_02'
            'moving camera':['I_MC_01', 'I_MC_02'],   #, 'I_MC_02'
            'occlusions':['I_OC_01', 'I_OC_02'],   #, 'I_OC_02'
            'simple sequences':['I_SI_01', 'I_SI_02'],   #, 'I_SI_02'
            #'simulated motion':['I_SM_01', 'I_SM_02', 'I_SM_03', 'I_SM_04', 'I_SM_05', 'I_SM_06', 'I_SM_07', 'I_SM_08', 'I_SM_09', 'I_SM_10', 'I_SM_11', 'I_SM_12'],   
}
dataset4 = {               

            'cloudy conditions':['O_CL_01', 'O_CL_02'],  #, 'O_CL_02'
            'moving camera':['O_MC_01', 'O_MC_02'], #, 'O_MC_02'
            'rainy conditions':['O_RA_01', 'O_RA_02'], #, 'O_RA_02'
            #'simulated motion':['O_SM_01', 'O_SM_02', 'O_SM_03', 'O_SM_04', 'O_SM_05', 'O_SM_06', 'O_SM_07', 'O_SM_08', 'O_SM_09', 'O_SM_10', 'O_SM_11', 'O_SM_12'], 
            'snowy conditions':['O_SN_01', 'O_SN_02'], #, 'O_SN_02'
            'sunny conditions':['O_SU_01', 'O_SU_02'],  #, 'O_SU_02'
}
"""
dataset_1 = [ 'Board', 'Candela_m1.10', 'CAVIAR1', 'CAVIAR2', 'CaVignal', 'Foliage', 'HallAndMonitor', 'HighwayI', 'HighwayII', 'HumanBody2', 'IBMtest2', 'PeopleAndFoliage', 'Snellen']

"""
"""
w= 0
x = 0
y=0
z=0
g=0
for category in dataset_1:   

            scene_list = dataset[category]

            for scene in scene_list:
		directory1 = '/home/cvprlab/backgroud-subtraction2/data/dataset_2014/training_100/'+category+'/'+scene+'/output'
		directory2 = '/home/cvprlab/backgroud-subtraction2/data/dataset_2014/training_100/'+category+'/'+scene+'/test'
		directory3 = '/home/cvprlab/backgroud-subtraction2/data/dataset_2014/training_100/'+category+'/'+scene+'/predicted'
		directory4 = '/home/cvprlab/backgroud-subtraction2/data/dataset_2014/training_100/'+category+'/'+scene+'/input'
		directory5 = '/home/cvprlab/backgroud-subtraction2/data/dataset_2014/training_100/'+category+'/'+scene+'/groundtruth'
   		if  os.path.exists(directory1):
			x +=1			
			os.rmdir(directory1)
		if  os.path.exists(directory2):
			y +=1	
			os.rmdir(directory2)
		if  os.path.exists(directory3):
			z +=1	
			os.rmdir(directory3)
			
       			os.makedirs(directory)
	        	
		if not os.path.exists(directory4):
			w +=1	
			os.mkdir(directory4)
		if not os.path.exists(directory5):
			g +=1	
			os.mkdir(directory5)
print(w)
print(x)
print(y)
print(z)
print(g)
"""

folder = r'C:\Users\santo\OneDrive\Desktop\soumendu_work\LASIESTA'
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

            #print('Output calculation for ->>> ' + category + ' / ' + scene + ' / ' + part)		
            image_path_list = glob.glob(os.path.join(folder+'\\'+category+'\\'+scene+'\\'+part+'\in_256\\'+'*bmp'))
            image_path_list = sorted(image_path_list)
            label_path_list = glob.glob(os.path.join(folder+"\\"+category+"\\"+scene+"\\"+part+"\gt_256\\"+"*png"))
            label_path_list = sorted(label_path_list)
            stop = int(0.5 * len(image_path_list[49:]))
            stop = 49 + stop
            if(len(image_path_list)==len(label_path_list)):
                x +=1
            #print(image_path_list[0])
            #print(image_path_list[9])
            
	    #for i,(image_path, label_path) in enumerate(zip(image_path_list[49:stop],label_path_list[49:stop])):
	    #	y +=1
	    #for i,(image_path, label_path) in enumerate(zip(image_path_list[stop:],label_path_list[stop:])):
	    #	v +=1
            for i,(image_path, label_path) in enumerate(zip(image_path_list[49:stop],label_path_list[49:stop])):
                w +=1
print(x)
#print(y)
#print(v)
#print(y+v)
print(w)

"""
folder = '/home/tyrone1/murari/Background/'
x = 0
y = 0
v=0
w=0
for category in dataset_1:   

                image_path_list = glob.glob(os.path.join(folder+category+'/'+'*png'))
                image_path_list = sorted(image_path_list)
                #stop = int(0.5 * len(image_path_list[49:]))
                #stop = 49 + stop
                if(len(image_path_list)>0):
                    x +=1
                #for i,(image_path, label_path) in enumerate(zip(image_path_list[49:stop],label_path_list[49:stop])):
	        #	y +=1
                #for i,(image_path, label_path) in enumerate(zip(image_path_list[stop:],label_path_list[stop:])):
				#	v +=1
                for i,(image_path) in enumerate(image_path_list[49:]):
					w +=1
print(x)
#print(y)
#print(v)
#print(y+v)
print(w)
"""
