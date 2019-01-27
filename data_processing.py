#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys
import pandas as pd

def organise_dataset():

    root_path = "/Users/Shared/SWD/TENSORFLOW-EXPERIMENTS"

    dataset_path = root_path+'/PV_SS'

    train_data = root_path+'/train/'

    os.makedirs (root_path, exist_ok=True)
    
    slideTable   = pd.read_csv(dataset_path+'/slideTable.csv')
    slideScanMap  = pd.read_csv(dataset_path+'/slideScanMap.csv')

    slideID__type =   {}
    scanID__type = {}

    for index, row in slideTable.iterrows():
        slideID__type.update({row["slideID"] : row["slideType_FK"]})

    for index, row in slideScanMap.iterrows():
        if (row["slideID_FK"] != "None"):
            slide_type = slideID__type [row["slideID_FK"]]
        else:    
            slide_type = "-99" # otherwise the lookup will not work    
        scanID__type.update({row["scanID_FK"] : slide_type})

    numberOfLy = 0
    numberOfTU = 0
    otherTypes = 0

    print("MAKE TRAINING DATA")
    testIndex = 0
    for i in range(0,7):
        dirname =  dataset_path + '/{0:02d}'.format(i)
        files = os.listdir(dirname)
        for file in files:
            scanid = file.replace ("_preview.jpg", "")
            slideType = scanID__type[scanid]
            command = "ln -s " + dirname + "/" + file + "  " + dataset_path 
            if (slideType == "2"):
                command += "/TRAINING/LY"
                numberOfLy += 1
            elif (slideType == "1"):
                command += "/TRAINING/TU"
                numberOfTU  += 1
            else:
                command += "/TRAINING/OTHERS"
                otherTypes  += 1
            command += "/" + file
            print (command)    
            os.system (command)

    print ("MAKE TEST DATA")    
    testIndex = 0
    for i in range(9,10):
        dirname =  dataset_path + '/{0:02d}'.format(i)
        files = os.listdir(dirname)        
        for file in files:
            scanid = file.replace ("_preview.jpg", "")
            slideType = scanID__type[scanid]
            command = "ln -s " + dirname + "/" + file + "  " + dataset_path 
            if (slideType == "2"):
                command += "/TEST/LY"
            elif (slideType == "28"):
                command += "/TEST/TU"
            else:
                command += "/TEST/OTHER"
            command +=  '_{0:04d}'.format(testIndex) + ".jpg"
            testIndex +=1
            print (command)    
            os.system (command)

    print (numberOfLy, otherTypes)

    print("Organising dataset by creating folders by slide type using names in labels done")
    return



def main():
    # Take folder path as in command line argument
    organise_dataset()

if __name__ == '__main__':
    main()
