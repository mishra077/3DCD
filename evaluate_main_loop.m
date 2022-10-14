clear all;clc;
SDB = input(strcat('Select DB Category: 1-badWeather|2-baseline|3-cameraJitter|4-dynamicBackground|',...
    '5-intermittentObjectMotion|6-lowFramerate|7-nightVideos|8-PTZ|9-shadow|10-thermal|11-turbulence'));

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
    display('1:ontinuousPan,2:intermittentPan,3:twoPositionPTZCam,4:zoomInZoomOut')
elseif(SDB==9)
    display('1:backdoor,2:bungalows,3:busStation,4:copyMachine,5:cubicle,6:peopleInShade')
elseif(SDB==10)
    display('1:corridor,2:diningRoom,3:lakeSide,4:library,5:park')                                    
else
    display('1:turbulence0,2:turbulence1,3:turbulence2,4:turbulence3')
end

subDB = input('Select DB No:');
database = {'badWeather', 'baseline', 'cameraJitter','dynamicBackground',...
    'intermittentObjectMotion', 'lowFramerate','nightVideos','PTZ','shadow', 'thermal',...
    'turbulence'};
db = {'blizzard','skating','snowFall','wetSnow','NA','NA';...
'highway','office','pedestrians','PETS2006','NA','NA';
'badminton','boulevard','sidewalk','traffic','NA','NA';...
'boats','canoe','fall','fountain01','fountain02','overpass';...
'abandonedBox','parking','sofa','streetLight','tramstop','winterDriveway';...
'port_0_17fps','tramCrossroad_1fps','tunnelExit_0_35fps','turnpike_0_5fps','NA','NA';...
'bridgeEntry','busyBoulvard','fluidHighway','streetCornerAtNight','tramStation','winterStreet';...
'continuousPan','intermittentPan','twoPositionPTZCam','zoomInZoomOut','NA','NA';...
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
'dontcare', 'dontcare', 'dontcare', 'dontcare','NA','NA';...
'2000', '1700', '1250', '3400', '7400', '1199';...
'5400', '3700', '6500', '4900', '600', 'NA';...
'2999', '2599', '2499', '1499', 'NA','NA'};


S_dB = database(SDB);
sub_dB = db(SDB,subDB);
videoPath = cell2mat(strcat('C:\Users\santo\OneDrive\Desktop\soumendu_work\dataset2014\',S_dB,'\',sub_dB,'\'));
%binaryFolder = 'D:\Dropbox\Papers Submitted to Journals\Conference Paper\CVPR - 2019\Results on CDNet 2014 Dataset\blizzard_predicted3';
binaryFolder= cell2mat(strcat('D:\soumendu_data\2dcd_median_result\',S_dB,'\',sub_dB,'\'));
startepoch=110;
endepoch=120;%52
for epoch = startepoch:endepoch
    epoch
    if epoch<10
        foldername =  strcat('e00',num2str(epoch));
    elseif epoch<100
        foldername =  strcat('e0',num2str(epoch));
    else
        foldername =  strcat('e',num2str(epoch));
    end
    binaryFolder2 = strcat(binaryFolder,'/','predicted_loop','/',foldername);
    % predicted_ch_last_batch
    idxTo_val = idxTo_Values(SDB,subDB);
%     idxTo_val = cell2mat(idxTo_val);
    processVideoFolder(videoPath, binaryFolder2,idxTo_val);
end

