clear all;clc;
SDB = input(strcat('Select DB Category: 1-badWeather|2-baseline|3-cameraJitter|4-dynamicBackground|',...
    '5-intermittentObjectMotion|6-lowFramerate|7-nightVideos|8-shadow|9-thermal|10-turbulence'));

if(SDB==1)
    display('1:blizzard,2:skating,3:snowFall,4:wetSnow')
elseif(SDB==2)
    display('1:highway,2:office,3:pedestrians,4:PETS2006')
elseif(SDB==3)
    display('1:badminton,2:boulevard,3:sidewalk,4:traffic')
elseif(SDB==4)
    display('1:boats,2:canoe,3:fall,4:fountain01,5:fountain02,6:overpass')
elseif(SDB==5)
    display('1:abandonedBox,2:parking,3:sofa,4:streetLight,5:tramstop,6:winterDriveway')
elseif(SDB==6)
    display('1:port_0_17fps,2:tramCrossroad_1fps,3:tunnelExit_0_35fps,4:turnpike_0_5fps')
elseif(SDB==7)
    display('1:bridgeEntry,2:busyBoulvard,3:fluidHighway,4:streetCornerAtNight,5:tramStation,6:winterStreet')
elseif(SDB==8)
    display('1:backdoor,2:bungalows,3:busStation,4:copyMachine,5:cubicle,6:peopleInShade')
elseif(SDB==9)
    display('1:corridor,2:diningRoom,3:lakeSide,4:library,5:park')                                    
else
    display('1:turbulence0,2:turbulence1,3:turbulence2,4:turbulence3')
end

%subDB = input('Select DB No:');
database = {'badWeather', 'baseline', 'cameraJitter','dynamicBackground',...
    'intermittentObjectMotion', 'lowFramerate','nightVideos','shadow', 'thermal',...
    'turbulence'};
db = {'blizzard','skating','snowFall','wetSnow','NA','NA';...
'highway','office','pedestrians','PETS2006','NA','NA';
'badminton','boulevard','sidewalk','traffic','NA','NA';...
'boats','canoe','fall','fountain01','fountain02','overpass';...
'abandonedBox','parking','sofa','streetLight','tramstop','winterDriveway';...
'port_0_17fps','tramCrossroad_1fps','tunnelExit_0_35fps','turnpike_0_5fps','NA','NA';...
'bridgeEntry','busyBoulvard','fluidHighway','streetCornerAtNight','tramStation','winterStreet';...
'backdoor','bungalows','busStation','copyMachine','cubicle','peopleInShade';...
'corridor','diningRoom','lakeSide','library','park','NA';...
'turbulence0','turbulence1','turbulence2','turbulence3','NA','NA'};

idxTo_Values = {'3949', '2349', '3649', '1999', 'NA','NA';...
'1700', '2050', '1099', '1200', 'NA','NA';...
'1150', '2500', '1200', '1570','NA','NA';...
'7999', '1189', '4000', '1184', '1499', '3000';...
'4500', '2500', '2750', '3200', '3200', '2500';...
'1999', '649', '2999', '1149','NA','NA';...
'1749', '1744', '881', '2999', '1749', '1339';...
'2000', '1700', '1250', '3400', '7400', '1199';...
'5400', '3700', '6500', '4900', '600', 'NA';...
'2999', '2599', '2499', '1499', 'NA','NA'};
% write propoer values
idxfrom_Values = {'1500', '750', '1400', '725', 'NA','NA';...
'591', '716', '375', '426', 'NA','NA';...
'151', '831', '176', '311','NA','NA';...
'3025', '170', '1476', '368','475', '976';...
'1001', '676', '1101', '1488', '916', '726';...
'475', '100', '475', '150','NA','NA';...
'350', '483', '216', '1075', '600', '195';...
'776', '676', '451', '1426', '3126', '450';...
'2426', '1476', '2726', '2126', '151', 'NA';...
'975', '675', '975', '325', 'NA','NA'};
Cat_video_arr = [4,4,4,6,6,4,6,6,5,4];

S_dB = database(SDB);
subDB = Cat_video_arr(SDB);

% videoPath = cell2mat(strcat('C:\Users\santo\OneDrive\Desktop\soumendu_work\dataset2014\',S_dB,'\',sub_dB,'\'));
% binaryFolder= cell2mat(strcat('C:\Users\santo\OneDrive\Desktop\soumendu_work\results_all_2dcd_median\',S_dB,'\',sub_dB,'\'));
videoPath = cell2mat(strcat('C:\Users\santo\OneDrive\Desktop\soumendu_work\dataset2014\',S_dB,'\'));
binaryFolder= cell2mat(strcat('D:\soumendu_data\2dcd_median_result\',S_dB,'\'));
startepoch=100;
endepoch=150;%52
All_results = zeros(endepoch-startepoch+1,2);
i=1;
for epoch = startepoch:endepoch
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
        idxTo_val = idxTo_Values(SDB,jj);
        idxfrom_val = idxfrom_Values(SDB,jj);
        binaryFolder3 = strcat(binaryFolder2,'/','predicted_loop','/',foldername);
        confusionMatrix = processVideoFolder3(videoPath2, binaryFolder3,idxTo_val, idxfrom_val);
        Precision = confusionMatrix(1)/(confusionMatrix(1)+confusionMatrix(2));
        %disp('Recall:');
        Recall = confusionMatrix(1)/(confusionMatrix(1)+confusionMatrix(3));
        %disp('Fscore:');
        F_Score = (2*Precision*Recall)/(Precision+Recall);
        F_Score_arr(jj,1) = F_Score;
        %disp('PWC:');
        PWC = 100*(confusionMatrix(2)+confusionMatrix(3))/(confusionMatrix(1)+confusionMatrix(2)+confusionMatrix(3)+confusionMatrix(4));
    end 
    avg_catwise=mean(F_Score_arr)
    All_results(i,1)= epoch;
    All_results(i,2)= avg_catwise;
    i=i+1;
end
filename = strcat(cell2mat(S_dB),'_category_avg_50p_test');
fileID2 = fopen(strcat(filename,'.txt'),'w');
fprintf(fileID2,'%d %1.4f\r\n',All_results');
fclose(fileID2);

