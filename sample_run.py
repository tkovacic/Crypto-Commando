#TITLE: cc_mgb_alpha.py
#AUTHOR: Timothy Damir Kovacic
#DATE-CREATED: 05/23/2021

import cbpro

import time
import logging
import os
import sys

import tensorflow as tf

import matplotlib.pyplot as plt
from datetime import date, datetime, timedelta

sys.path.append("./Engine");
sys.path.append("./Models");
from cc_engine import cc_cycle

global st;
st = time.time();
global cycle_count;
cycle_count = 0;
global increment_pace;
increment_pace = 120;

global tv1;
tv1 = 3;
global tbp1;
tbp1 = 1000000;
global tsp1;
tsp1 = 0;

global OKCYAN;
OKCYAN = '\033[96m';
global OKGREEN;
OKGREEN = '\033[92m';
global FAIL;
FAIL = '\033[91m';

logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',datefmt='%Y-%m-%d:%H:%M:%S',level=logging.ERROR);
logger = logging.getLogger(__name__);

print("Reconstructing DNN Models...");
grtModel = tf.keras.models.load_model("Models/dnnGRTModel.h5");
print("Loaded GRT DNN model!");
print("DONE\n");

while True:
    os.system('cls');
    output = cc_cycle("GRT-USD",grtModel,tv1,tbp1,tsp1);
    output = str(output).split("||");
    tbp1 = output[1];
    tsp1 = output[2];

    time.sleep(increment_pace - ((time.time() - st) % increment_pace));
