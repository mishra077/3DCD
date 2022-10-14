clear all;clc;
SDB = input(strcat('Select DB Category: 1-Indoor Sequences|2-Outdoor Sequences'));
if(SDB==1)
    display('1:bootstrap, 2:camouflage, 3:illumination changes, 4:modified background, 5: moving camera, 6:occlusions, 7:simple sequences, 8:simulated motion');
else
    display('1:cloudy conditions, 2:moving camera, 3:rainy conditions, 4:simulated motion, 5:snowy conditions, 6:sunny conditions')
end

subDB = input('Select DB No:');
database = {'Indoor Sequences', 'Outdoor Sequences'};
db = {'bootstrap', 'camouflage', 'illumination changes', 'modified background', 'moving camera', 'occlusions', 'simple sequences', 'simulated motion';...
'cloudy conditions', 'moving camera', 'rainy conditions', 'simulated motion', 'snowy conditions', 'sunny conditions','NA','NA'};

if(SDB==1 && subDB==1)
    display('1:I_BS_01, 2:I_BS_02');
elseif(SDB==1 && subDB==2)
    display('1:I_CA_01, 2:I_CA_02');
elseif(SDB==1 && subDB==3)
    display('1:I_IL_01, 2:I_IL_02');
elseif(SDB==1 && subDB==4)
    display('1:I_MB_01, 2:I_MB_02');
elseif(SDB==1 && subDB==5)
    display('1:I_MC_01, 2:I_MC_02');   
elseif(SDB==1 && subDB==6)
    display('1:I_OC_01, 2:I_OC_02'); 
elseif(SDB==1 && subDB==7)
    display('1:I_SI_01, 2:I_SI_02');  
elseif(SDB==1 && subDB==8)
    display('1:I_SM_01, 2:I_SM_02, 3:I_SM_03, 4:I_SM_04, 5:I_SM_05, 6:I_SM_06, 7:I_SM_07, 8:I_SM_08, 9:I_SM_09, 10:I_SM_10, 11:I_SM_11, 12:I_SM_12');
end

if(SDB==2 && subDB==1)
    display('1:O_CL_01, 2:O_CL_02');
elseif(SDB==2 && subDB==2)
    display('1:O_MC_01, 2:O_MC_02');
elseif(SDB==2 && subDB==3)
    display('1:O_RA_01, 2:O_RA_02');
elseif(SDB==2 && subDB==4)
    display('1:O_SM_01, 2:O_SM_02, 3:O_SM_03, 4:O_SM_04, 5:O_SM_05, 6:O_SM_06, 7:O_SM_07, 8:O_SM_08, 9:O_SM_09, 10:O_SM_10, 11:O_SM_11, 12:O_SM_12');
elseif(SDB==2 && subDB==5)
    display('1:O_SN_01, 2:O_SN_02');
elseif (SDB==2 && subDB==6)
    display('1:O_SU_01, 2:O_SU_02');
end
sub_subDB = input('Select sub_subDB No:');
db_1 = {'I_BS_01', 'I_BS_02', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA'; 
	   'I_CA_01', 'I_CA_02', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA'; 
       'I_IL_01', 'I_IL_02', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA';  
	   'I_MB_01', 'I_MB_02', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA';   
       'I_MC_01', 'I_MC_02', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA';   
       'I_OC_01', 'I_OC_02', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA';   
       'I_SI_01', 'I_SI_02', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA';   
       'I_SM_01', 'I_SM_02', 'I_SM_03', 'I_SM_04', 'I_SM_05', 'I_SM_06', 'I_SM_07', 'I_SM_08', 'I_SM_09', 'I_SM_10', 'I_SM_11', 'I_SM_12'   
};
db_1_count = {'275', '275', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA';
              '350','525', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA';
              '300', '525', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA';
              '450', '350', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA';
              '300', '250', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA';
              '250', '250', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA';
              '300', '300', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA';
              '300','300','300','300','300','300','300','300','300','300','300','300'};
db_2 = {'O_CL_01', 'O_CL_02', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA'; 
        'O_MC_01', 'O_MC_02', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA'; 
        'O_RA_01', 'O_RA_02', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA'; 
        'O_SM_01', 'O_SM_02', 'O_SM_03', 'O_SM_04', 'O_SM_05', 'O_SM_06', 'O_SM_07', 'O_SM_08', 'O_SM_09', 'O_SM_10', 'O_SM_11', 'O_SM_12'; 
        'O_SN_01', 'O_SN_02', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA'; 
        'O_SU_01', 'O_SU_02', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA'};  
db_2_count = {'225', '425', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA';
              '425', '175', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA';
              '1400', '375', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA';
              '425','425','425','425','425','425','425','425','425','425','425','425';
              '500', '850', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA';
              '250', '400', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA'};
            
S_dB = database(SDB);
sub_dB = db(SDB,subDB);
if (SDB==1)
    sub_sub_dB = db_1(subDB,sub_subDB);
    idxToValue = db_1_count(subDB,sub_subDB);
else
    sub_sub_dB = db_2(subDB,sub_subDB);
    idxToValue = db_2_count(subDB,sub_subDB);
end
videoPath = cell2mat(strcat('C:\Users\santo\OneDrive\Desktop\soumendu_work\LASIESTA\',S_dB,'\',sub_dB,'\',sub_sub_dB,'\'));
%binaryFolder = 'D:\Dropbox\Papers Submitted to Journals\Conference Paper\CVPR - 2019\Results on CDNet 2014 Dataset\blizzard_predicted3';
binaryFolder=cell2mat(strcat('C:\Users\santo\OneDrive\Desktop\soumendu_work\lasiesta_results\',S_dB,'\',sub_dB,'\',sub_sub_dB,'\'));
dscrptr = sub_sub_dB;
startepoch=84;
endepoch=84;%52
for epoch = startepoch:endepoch
    epoch
    if epoch<10
        foldername =  strcat('e00',num2str(epoch));
    elseif epoch<100
        foldername =  strcat('e0',num2str(epoch));
    else
        foldername =  strcat('e',num2str(epoch));
    end
    binaryFolder2 = strcat(binaryFolder,'predicted','\',foldername);
    % predicted_ch_last_batch
    %idxTo_val = str2num(idxToValue);
%     idxTo_val = cell2mat(idxTo_val);
    processVideoFolder_lasiesta(videoPath, binaryFolder2,dscrptr,idxToValue);
end
