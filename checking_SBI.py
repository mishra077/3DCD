import os
import glob

dataset_1 = [ 'Board', 'Candela_m1.10', 'CAVIAR1', 'CAVIAR2', 'CaVignal', 'Foliage', 'HallAndMonitor',
             'HighwayI', 'HighwayII', 'HumanBody2', 'IBMtest2', 'PeopleAndFoliage', 'Snellen', 'Toscana']

folder = 'G:\FgSegNet-master\SBI2015_dataset'
x = 0
y = 0
v=0
w=0
for category in dataset_1:  

    image_path_list = glob.glob(os.path.join(folder+'\\'+category+'\in_256\\'+'*g'))
    image_path_list = sorted(image_path_list)
    label_path_list = glob.glob(os.path.join(folder+'\\'+category+'\gt_256\\'+'*g'))
    label_path_list = sorted(label_path_list)
    stop = int(0.5 * len(image_path_list[49:]))
    stop = 49 + stop

            #print('Output calculation for ->>> ' + category + ' / ' + scene + ' / ' + part)		
    if(len(image_path_list)==len(label_path_list)):
        x +=1
    for i,(image_path, label_path) in enumerate(zip(image_path_list[49:stop],label_path_list[49:stop])):
        w +=1
print(x)
#print(y)
#print(v)
#print(y+v)
print(w)