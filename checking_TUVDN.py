import os
import glob


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

folder = r'G:\TU-VDN'
x = 0
y = 0
v=0
w=0
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
            print(os.path.join(folder+'\\'+category+'\\'+scene+'\\'+part+'_in_256'))
            path1= os.path.join(folder+'\\'+category+'\\'+scene+'\\'+part+'_in_256')
            if  os.path.exists(path1):
                y=y+1
            #print('Output calculation for ->>> ' + category + ' / ' + scene + ' / ' + part)		
            image_path_list = glob.glob(os.path.join(folder+'\\'+category+'\\'+scene+'\\'+part+'_in_256\\'+'*bmp'))
            image_path_list = sorted(image_path_list)
            label_path_list = glob.glob(os.path.join(folder+"\\"+category+"\\"+scene+"\\"+part+"_GT_gt_256\\"+"*bmp"))
            label_path_list = sorted(label_path_list)
	        #stop = int(0.6 * len(image_path_list[49:]))
            #stop = 49 + stop
            #print(image_path_list[0])
            #print(image_path_list[9])
            
	    #for i,(image_path, label_path) in enumerate(zip(image_path_list[49:stop],label_path_list[49:stop])):
	    #	y +=1
	    #for i,(image_path, label_path) in enumerate(zip(image_path_list[stop:],label_path_list[stop:])):
	    #	v +=1
            for i, label_path in enumerate(label_path_list[4:]):
                w +=1
print(x)
print(y)
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
