clear all;clc;
SDB = input(strcat('Select DB Category: 1-fgsegnet|2-2dcd'));
if(SDB==1)
    display('1:bootstrap, 2:camouflage, 3:illumination changes, 4:modified background, 5: moving camera, 6:occlusions, 7:simple sequences, 8:simulated motion');
else
    display('1:cloudy conditions, 2:moving camera, 3:rainy conditions, 4:simulated motion, 5:snowy conditions, 6:sunny conditions')
end
database = {'fgsegnet', '2dcd'};
%%%%%%Scene Independent%%%%%% remove the unnecessary videos and the
%%%%%%corresponding frame counts
%db_1 = {'Board', 'Candela_m1.10', 'CAVIAR1', 'CAVIAR2', 'CaVignal', 'Foliage','HallAndMonitor',...
%'HighwayI', 'HighwayII', 'HumanBody2', 'IBMtest2', 'PeopleAndFoliage', 'Snellen'};

%db_1_count = {'228','350', '610', '460', '258', '389',...
%'296', '440', '500', '740', '90', '341', '321'};

%db_2 = {'Board', 'Candela_m1.10', 'CAVIAR1', 'CAVIAR2', 'CaVignal', 'Foliage','HallAndMonitor',...
%'HighwayI', 'HighwayII', 'HumanBody2', 'IBMtest2', 'PeopleAndFoliage', 'Snellen'};

%db_2_count = {'179', '349', '561', '411', '209', '340', '247',...
%'391', '451', '691', '41', '292', '272'};
%%%%% Scene Dependent%%%%
db_1 = {'Board', 'Candela_m1.10', 'CAVIAR1', 'CAVIAR2', 'CaVignal', 'Foliage','HallAndMonitor',...
'HighwayI', 'HighwayII', 'HumanBody2', 'IBMtest2', 'PeopleAndFoliage', 'Snellen'};

db_1_count = {'228','350', '610', '460', '258', '389',...
'296', '440', '500', '740', '90', '341', '321'};

db_2 = {'Board', 'Candela_m1.10', 'CAVIAR1', 'CAVIAR2', 'CaVignal', 'Foliage','HallAndMonitor',...
'HighwayI', 'HighwayII', 'HumanBody2', 'IBMtest2', 'PeopleAndFoliage', 'Snellen'};

db_2_count = {'179', '349', '561', '411', '209', '340', '247',...
'391', '451', '691', '41', '292', '272'};
% ground-truth path
videoPath = 'G:\FgSegNet-master\SBI2015_dataset\';
% results-path
binaryFolder='G:\2dcd_results\Results_2dcd_combine_SBI\';
%dscrptr = sub_sub_dB;
%All_results = zeros(endepoch-startepoch+1,2);
i=1;
startepoch=18;
endepoch=18;%52
for epoch = startepoch:endepoch
    S_dB = database(SDB);
    epoch
    if epoch<10
        foldername =  strcat('e00',num2str(epoch));
    elseif epoch<100
        foldername =  strcat('e0',num2str(epoch));
    else
        foldername =  strcat('e',num2str(epoch));
    end    
    F_Score_arr = zeros(subDB,1);
    for jj = 1:13
        if (SDB==1)
            sub_dB = db_1(jj);
            idxToValue = db_1_count(jj);
        else
            sub_dB = db_1(jj);
            idxToValue = db_1_count(jj);
        end
        sub_dB = cell2mat(sub_dB);
        videoPath2 = strcat(videoPath, sub_dB,'\');
        binaryFolder2 = strcat(binaryFolder,sub_dB,'\');
        binaryFolder3 = strcat(binaryFolder2,'\','predicted_loop','\',foldername);
        dscrptr = sub_dB;
        processVideoFolder_sbi(videoPath3, binaryFolder3,dscrptr,idxToValue);
    end
end
