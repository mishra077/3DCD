# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 17:49:55 2019

@author: MEMS_Santosh_WS
"""

from keras.models import Model
from keras.layers import Activation, Input
from keras.layers.convolutional import Conv2D, Conv2DTranspose, Conv3D, Conv3DTranspose
from keras.layers import Add, Concatenate, Subtract
from keras.layers import BatchNormalization
from keras.layers import Dropout
from keras.layers import UpSampling2D, UpSampling3D
from keras.layers import MaxPooling3D as mp3d
from keras.layers import AveragePooling3D as ap3d
from keras.optimizers import Adam
import keras.backend as K
from keras.utils import plot_model
from keras.layers.advanced_activations import LeakyReLU
from keras.optimizers import SGD
K.set_image_dim_ordering('th')

class MSFgNet(object):

    def __init__(self, img_shape, img_shape2):
        self.img_shape = img_shape
        self.img_shape2 = img_shape2

    def MSFgNet(self, input_shape, input_shape2):

        #input_shape = Input([50, 256, 256, 1])
        #input_shape2 = Input([1, 256, 256, 1])    
        model = Conv3D(32, (3, 3, 3), strides = (1, 1, 1), padding = 'same', data_format = 'channels_last')(input_shape)
        model = ap3d(pool_size=(5, 3, 3), strides = (5, 1, 1), padding = 'same', data_format = 'channels_last')(model)
        model = Activation('relu')(model)
                
        model = Conv3D(16, (3, 3, 3), strides = 1, padding = 'same', data_format = 'channels_last')(model)
        model = ap3d(pool_size = (2, 3, 3), strides = (2, 1, 1), padding = 'same', data_format = 'channels_last')(model)        
        model = Activation('relu')(model)

        model = Conv3D(8, (3, 3, 3), strides = 1, padding = 'same', data_format = 'channels_last')(model)
        model = ap3d(pool_size = (5, 3, 3), strides = (5, 1, 1), padding = 'same', data_format = 'channels_last')(model)
        model = Activation('relu')(model)

        #model = Conv3D(4, (3, 3, 3), strides = 1, padding = 'same', data_format = 'channels_last')(model)
        #model = mp3d(pool_size = (3, 3, 3), strides = (5, 1, 1), padding = 'same', data_format = 'channels_last')(model)
        #model = Activation('relu')(model)
        

        bg = Conv3D(1, (1, 3, 3), padding = 'same', data_format = 'channels_last')(model)
        bg = Activation('relu')(bg)
        
        #result = Model(inputs = [input_dim, input_dim2], outputs = bg)
        #print(result.summary())

        #bg_estim = Subtract()([input_shape2, bg])


        model = Conv3D(8, (1, 3, 3), padding = 'same', data_format = 'channels_last')(bg)
        model2 = Conv3D(8, (1, 3, 3), padding = 'same', data_format = 'channels_last')(input_shape2)
        model = Concatenate(axis = -1)([ model, model2])
        model = Activation('relu')(model)

        #Block-10
        #model = Conv3D(16, (3, 3, 3), strides = (1, 1, 1), padding = 'same', data_format = 'channels_last')(model)
        #model = Activation('relu')(model)
        #x_ip = Conv3D(16, (3, 3, 3), strides = (2, 2, 1), padding ='same', data_format = 'channels_last')(model)
        #x_ip = Activation('relu')(x_ip)
        #y_ip =Conv3D(16, (3, 3, 3), strides = (4, 4, 1), padding = 'same', data_format = 'channels_last')(model)
        #y_ip = Activation('relu')(y_ip)
        #model = mp3d(pool_size = (1, 1, 1), padding = 'same', data_format = 'channels_last')(model)
        x_ip = mp3d(pool_size = (1, 2, 2), padding = 'same', data_format = 'channels_last')(model)
        y_ip = mp3d(pool_size = (1, 4, 4), padding = 'same', data_format = 'channels_last')(model)

        #Block-10.1
        #x_ip = Conv3D(16, (3, 3, 3), strides = 1, padding = 'same', data_format = 'channels_last')(x_ip)
        #x_ip = Activation('relu')(x_ip)

        x_ip = Conv3D(16, (1, 3, 3), strides = 1, padding = 'same', data_format = 'channels_last')(x_ip)
        x_ip = mp3d(pool_size = (1, 2, 2), padding = 'same', data_format = 'channels_last')(x_ip)
        x_ip = Activation('relu')(x_ip)


        #Block-10.2
        #model = Conv3D(16, (3, 3, 3), strides = 1, padding = 'same', data_format = 'channels_last')(model)
        #model = Activation('relu')(model)

        model = Conv3D(16, (1, 3, 3), strides = 1, padding = 'same', data_format = 'channels_last')(model)
        model = mp3d(pool_size = (1, 2, 2), padding = 'same', data_format = 'channels_last')(model)
        model = Activation('relu')(model)


        model = Conv3D(16, (1, 3, 3), strides = 1, padding = 'same', data_format = 'channels_last')(model)
        model = mp3d(pool_size = (1, 2, 2), padding = 'same', data_format = 'channels_last')(model)
        model = Activation('relu')(model)

        #Block-10.3
        y_ip = Conv3D(16, (1 , 3, 3), strides = 1, padding = 'same', data_format = 'channels_last')(y_ip)
        #y_ip = mp3d(pool_size = (2, 2, 1), padding = 'same', data_format = 'channels_last')(y_ip)
        y_ip = Activation('relu')(y_ip)

        #Block-11
        Sum = Concatenate(axis = -1)([x_ip, model, y_ip])
        res1 = Sum
        Sum = Conv3D(48, (1, 3, 3), padding = 'same', data_format = 'channels_last')(Sum)
        Sum2 = Add()([res1, Sum])
        Sum2 = Activation('relu')(Sum2)
        
        res2 = Sum2
        Sum2 = Conv3D(48, (1, 3, 3), padding = 'same', data_format = 'channels_last')(Sum2)
        Sum3 = Add()([res2, Sum2])
        Sum3 = Activation('relu')(Sum3)

        #DECODER

        #Block-13.1
        #x2_ip = Conv3DTranspose(16, (3, 3, 3), strides = (2, 2, 1), padding = 'same', data_format = 'channels_last')(Sum3)
        x2_ip = UpSampling3D(size = (1, 2, 2), data_format = 'channels_last')(Sum3)
        #x2_ip = Activation('relu')(x2_ip)

        x2_ip  = Conv3DTranspose(32, (1, 3, 3) , padding = 'same', data_format = 'channels_last')(x2_ip)
        x2_ip = mp3d(pool_size = (1, 3, 3), strides = 1, padding = 'same', data_format = 'channels_last')(x2_ip)
        x2_ip = Activation('relu')(x2_ip)

        x2_ip  = Conv3DTranspose(16, (1, 3, 3) , padding = 'same', data_format = 'channels_last')(x2_ip)
        x2_ip = mp3d(pool_size = (1, 3, 3), strides = 1, padding = 'same', data_format = 'channels_last')(x2_ip)
        x2_ip = Activation('relu')(x2_ip)
        
        #x2_ip  =Conv3DTranspose(16, (3, 3, 3),strides = (2, 2, 1), padding = 'same', data_format = 'channels_last')(x2_ip)
        x2_ip = UpSampling3D(size = (1, 2, 2), data_format = 'channels_last')(x2_ip)
        x2_ip = Activation('relu')(x2_ip) #changed
       
        #Block-13.2
        #model_2 = Conv3DTranspose(16, (3, 3, 3), strides = (2, 2, 1), padding = 'same', data_format = 'channels_last')(Sum3)
        model_2 = UpSampling3D(size = (1, 2, 2), data_format = 'channels_last')(Sum3)       
        #model_2 = Activation('relu')(model_2)

        model_2  = Conv3DTranspose(32, (1, 3, 3) , padding = 'same', data_format = 'channels_last')(model_2)
        model_2 = mp3d(pool_size = (1, 3, 3), strides = 1, padding = 'same', data_format = 'channels_last')(model_2)
        model_2 = Activation('relu')(model_2)

        #model_2 = Conv3DTranspose(16, (3, 3, 3), strides = (2, 2, 1), padding = 'same', data_format = 'channels_last')(model_2)
        model_2 = UpSampling3D(size = (1, 2, 2), data_format = 'channels_last')(model_2)  
        #model_2 = Activation('relu')(model_2)

        model_2  = Conv3DTranspose(16, (1, 3, 3) , padding = 'same', data_format = 'channels_last')(model_2)
        model_2 = mp3d(pool_size = (1, 3, 3), strides = 1, padding = 'same', data_format = 'channels_last')(model_2)
        model_2 = Activation('relu')(model_2)

        #Block-13.3
        #y2_ip = Conv3DTranspose(16, (3, 3, 3), strides = (2, 2, 1), padding = 'same', data_format = 'channels_last')(Sum3)
        y2_ip = UpSampling3D(size = (1, 4, 4), data_format = 'channels_last')(Sum3) # 64 x64
        #y2_ip = Activation('relu')(y2_ip)
        
        #y2_ip = Conv3DTranspose(16, (3, 3, 3), strides = (2, 2, 1), padding = 'same', data_format = 'channels_last')(y2_ip) # 64 x64
        #y2_ip = UpSampling3D(size = (2, 2, 1), data_format = 'channels_last')(y2_ip)
        #y2_ip = Activation('relu')(y2_ip)

        y2_ip  = Conv3DTranspose(32, (1, 3, 3) , padding = 'same', data_format = 'channels_last')(y2_ip)
        y2_ip = mp3d(pool_size = (1, 3, 3), strides = 1, padding = 'same', data_format = 'channels_last')(y2_ip)
        y2_ip = Activation('relu')(y2_ip)

        y2_ip  = Conv3DTranspose(16, (1, 3, 3) , padding = 'same', data_format = 'channels_last')(y2_ip)
        y2_ip = mp3d(pool_size = (1, 3, 3), strides = 1, padding = 'same', data_format = 'channels_last')(y2_ip)
        y2_ip = Activation('relu')(y2_ip)

        #Block-15
        Sum4 = Concatenate(axis = -1)([x2_ip, model_2, y2_ip])
        #Sum4 = Activation('relu')(Sum4) #changed

        #Block-16

        Sum4 = Conv3D(16, (1, 3, 3), padding = 'same', data_format = 'channels_last')(Sum4) 
        Sum4 = Activation('relu')(Sum4)

        #Sum4 = Conv3DTranspose(16, (3, 3, 3), padding = 'same', data_format = 'channels_last')(Sum4)
        #Sum4 = Activation('relu')(Sum4)

        Sum4 = Conv3D(8, (1, 3, 3), padding = 'same', data_format = 'channels_last')(Sum4)
        Sum4 = Activation('relu')(Sum4)
 
        Sum4 = Conv3D(1, (1, 3, 3), padding = 'same', data_format = 'channels_last')(Sum4)
        Sum4 = Activation('sigmoid')(Sum4)

        #result = Model(inputs = [input_shape, input_shape2], outputs = Sum4)
        #print(result.summary())

        #plot_model(result, to_file = 'msfgnet.png')

        return Sum4


    def initModel_3D(self):

        depth, height, width = self.img_shape
        depth2, height2, width2 = self.img_shape2
        input_dimension = Input(shape = (depth, height, width, 1), name="main_input")
        input_dimension2 = Input(shape = (depth2, height2, width2, 1), name="aux_input")
        net_op = self.MSFgNet(input_dimension, input_dimension2)
        net_model = Model(inputs = [input_dimension, input_dimension2], outputs = net_op)

        sgd = SGD(lr = 8e-04, decay = 0, nesterov = True) #for 50-50 scene = 1e-03,,,, for 50% 5e-04   #decay = 1e-05
        net_model.compile(optimizer = sgd, loss = 'binary_crossentropy', metrics = ['accuracy'])

        return net_model
    
    
#from contextlib import redirect_stdout

#with open('modelsummary2.txt', 'w') as f:
#    with redirect_stdout(f):
#        result.summary()



