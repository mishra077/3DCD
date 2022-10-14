clear all;clc;
SDB = input(strcat('Select DB Category: 1-Indoor Sequences|2-Outdoor Sequences'));
if(SDB==1)
    display('1:bootstrap, 2:camouflage, 3:illumination changes, 4:modified background, 5: moving camera, 6:occlusions, 7:simple sequences, 8:simulated motion');
else
    display('1:cloudy conditions, 2:moving camera, 3:rainy conditions, 4:simulated motion, 5:snowy conditions, 6:sunny conditions')
end

%subDB = input('Select DB No:');
database = {'Indoor Sequences', 'Outdoor Sequences'};
db = {'bootstrap', 'camouflage', 'illumination changes', 'modified background', 'moving camera', 'occlusions', 'simple sequences', 'simulated motion';...
'cloudy conditions', 'moving camera', 'rainy conditions', 'snowy conditions', 'sunny conditions','simulated motion', 'NA','NA'};
%sub_subDB = input('Select sub_subDB No:');
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
        'O_SN_01', 'O_SN_02', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA'; 
        'O_SU_01', 'O_SU_02', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA';
        'O_SM_01', 'O_SM_02', 'O_SM_03', 'O_SM_04', 'O_SM_05', 'O_SM_06', 'O_SM_07', 'O_SM_08', 'O_SM_09', 'O_SM_10', 'O_SM_11', 'O_SM_12'};  
db_2_count = {'225', '425', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA';
              '425', '175', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA';
              '1400', '375', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA';
              '500', '850', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA';
              '250', '400', 'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA';
              '425','425','425','425','425','425','425','425','425','425','425','425';};
            

Cat_video_arr = [7,5];
Cat_video_arr_1 = [2, 2, 2, 2, 2, 2, 2];
Cat_video_arr_2 = [2, 2, 2, 2, 2];

S_dB = database(SDB);
subDB = Cat_video_arr(SDB);

%videoPath = cell2mat(strcat('C:\Users\santo\OneDrive\Desktop\soumendu_work\LASIESTA\',S_dB,'\',sub_dB,'\',sub_sub_dB,'\'));
videoPath = cell2mat(strcat('C:\Users\santo\OneDrive\Desktop\soumendu_work\LASIESTA\',S_dB,'\'));
%binaryFolder = 'D:\Dropbox\Papers Submitted to Journals\Conference Paper\CVPR - 2019\Results on CDNet 2014 Dataset\blizzard_predicted3';
%binaryFolder=cell2mat(strcat('G:\Results_3dcd_L\',S_dB,'\',sub_dB,'\',sub_sub_dB,'\'));
binaryFolder=cell2mat(strcat('G:\2dcd_results\Results_2dcd_50p-50p_combine_L\',S_dB,'\'));
%dscrptr = sub_sub_dB;
%All_results = zeros(endepoch-startepoch+1,2);
i=1;

startepoch=36;
endepoch=36;%52
for epoch = startepoch:endepoch
    S_dB = database(SDB);
    sub_dB = db(SDB,subDB);
    %if (SDB==1)
    %    sub_sub_dB = 7;
    %else
    %    sub_sub_dB = 5;        
    %end

    epoch
    if epoch<10
        foldername =  strcat('e00',num2str(epoch));
    elseif epoch<100
        foldername =  strcat('e0',num2str(epoch));
    else
        foldername =  strcat('e',num2str(epoch));
    end
    
        F_Score_arr = zeros(subDB,1);
    for jj = 1:subDB
        sub_dB = cell2mat(db(SDB,jj));
        videoPath2 = strcat(videoPath, sub_dB,'\');
        binaryFolder2 = strcat(binaryFolder,sub_dB,'\');
        
        for gg = 1:2
            if (SDB==1)
                sub_sub_dB = db_1(jj,gg);
                idxToValue = db_1_count(jj,gg);
            else
                sub_sub_dB = db_2(jj,gg);
                idxToValue = db_2_count(jj,gg);
            end

            %idxTo_val = idxTo_Values(SDB,jj);
            %idxfrom_val = idxfrom_Values(SDB,jj);
            binaryFolder3 = strcat(binaryFolder2,sub_sub_dB,'\','predicted_loop','\',foldername);
            videoPath3 = strcat(videoPath2,sub_sub_dB,'\');
            %binaryFolder4 = strcat(binaryFolder2,'/','predicted_loop','/',foldername);
            dscrptr = cell2mat(sub_sub_dB);
            processVideoFolder_lasiesta_50p(videoPath3, binaryFolder3,dscrptr,idxToValue);
            %Precision = confusionMatrix(1)/(confusionMatrix(1)+confusionMatrix(2));
            %disp('Recall:');
            %Recall = confusionMatrix(1)/(confusionMatrix(1)+confusionMatrix(3));
            %disp('Fscore:');
            %F_Score = (2*Precision*Recall)/(Precision+Recall);
            %F_Score_arr(jj,1) = F_Score;
            %disp('PWC:');
            %PWC = 100*(confusionMatrix(2)+confusionMatrix(3))/(confusionMatrix(1)+confusionMatrix(2)+confusionMatrix(3)+confusionMatrix(4));
        end
    end 
    
    
    
    %binaryFolder2 = strcat(binaryFolder,'predicted','\',foldername);
    % predicted_ch_last_batch
    %idxTo_val = str2num(idxToValue);
%     idxTo_val = cell2mat(idxTo_val);
    %processVideoFolder_lasiesta(videoPath, binaryFolder2,dscrptr,idxToValue);
end
