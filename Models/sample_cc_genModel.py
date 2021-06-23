#sample_cc_genModel.py
#Author: Timothy Damir Kovacic
#Created 6/12/2021

import os
import sys
import time
import logging
import cbpro
import math
from datetime import date, datetime, timedelta

import tensorflow.compat.v2.feature_column as fc
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

#variables
global OKCYAN;
OKCYAN = '\033[96m';
global OKGREEN;
OKGREEN = '\033[92m';
global FAIL;
FAIL = '\033[91m';
global WARN;
WARN = '\033[93m';

logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',datefmt='%Y-%m-%d:%H:%M:%S',level=logging.ERROR);
logger = logging.getLogger(__name__);

model = Sequential();
model.add(LSTM(units=5, return_sequences=True, batch_input_shape=(1, 1, 2), input_shape=(1, 2)));
model.add(Dropout(0.1));
model.add(Dense(units=1));
model.compile(optimizer='adam', loss='mean_squared_error');

model.save("Models/dnn1INCHModel.h5");
model.save("Models/dnnAAVEModel.h5");
model.save("Models/dnnALGOModel.h5");
model.save("Models/dnnANKRModel.h5");
