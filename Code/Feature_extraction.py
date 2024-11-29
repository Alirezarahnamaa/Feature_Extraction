import os
from os.path import exists
import cv2
import numpy as np
from decimal import *
import tensorflow
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.models import Model

OS_PATH_STYLE = '/'
SAVE_ROOT_PATH = 'Resnet_UCF11_features'
DATASET_PATH = '/UCF11/'

INPUT_SHAPE = (240, 320, 3)
CLASS_ABLE_SAVE = True
# Global Value
classesPath = []
xTrain = []
xTest = []
yTrain = []
yTest = []

def resnet50():

    cnn_model= tensorflow.keras.applications.ResNet50(input_shape= INPUT_SHAPE , include_top=False, weights='imagenet',pooling = 'avg')#=2048
    for layer in cnn_model.layers:
        layer.trainable=False
    return cnn_model

def FeatureExtraction(videodata, ResnetModel , finalVideoResult:list):
    CNN_Export = []   
    for frame in videodata:
        y = np.expand_dims(frame, axis=0)
        w = preprocess_input(y)
        #w = preprocess_input(frame)
        CNN_Export.append(ResnetModel.predict(w))
    finalVideoResult.append(CNN_Export )
      
def CreateVideoResult(data, ResnetModel, fileCount=-1):
    videodata = data
    finalVideoResult = []

    FeatureExtraction(videodata, ResnetModel, finalVideoResult)
    return finalVideoResult

def SaveResult(result, fileName, className=''):
    path = SAVE_ROOT_PATH
    print(className)
    if CLASS_ABLE_SAVE == True:
        path = SAVE_ROOT_PATH+OS_PATH_STYLE+className
        if exists(path) == False:
            path = SAVE_ROOT_PATH+OS_PATH_STYLE+className
            print(path)
            os.makedirs(path)

    array_result = np.asarray(result)
    np.savez_compressed(path+OS_PATH_STYLE+fileName+'.npz', array_result)



trainData = 'Train Data'
testData = 'Test Data'
Label = 'save labels as a npz file'
ResnetModel = resnet50()

trainData = CreateVideoResult(Label, TrainData, ResnetModel)
testData = CreateVideoResult( label, testData, ResnetModel)