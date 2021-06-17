#TITLE: cc_mgb_echo.py
#AUTHOR: Timothy Damir Kovacic
#DATE-CREATED: 05/23/2021

import cbpro

import time
import logging
import os
import sys

import tensorflow as tf
sys.path.append("../Util");

from datetime import date, datetime, timedelta
from cc_engine import cc_cycle

global st;
st = time.time();
global cycle_count;
cycle_count = 0;
global increment_pace;
increment_pace = 300;

global tv1;
tv1 = 1.5;
global demastate1;
demastate1 = "";
global tbp1;
tbp1 = 1000000;
global tsp1;
tsp1 = 0;
global cc1;
cc1 = 0;

global tv2;
tv2 = 0.25;
global demastate2;
demastate2 = "";
global tbp2;
tbp2 = 1000000;
global tsp2;
tsp2 = 0;
global cc2;
cc2 = 0;

global tv3;
tv3 = 14;
global demastate3;
demastate3 = "";
global tbp3;
tbp3 = 1000000;
global tsp3;
tsp3 = 0;
global cc3;
cc3 = 0;

global tv4;
tv4 = 0.15;
global demastate4;
demastate4 = "";
global tbp4;
tbp4 = 1000000;
global tsp4;
tsp4 = 0;
global cc4;
cc4 = 0;

global tv5;
tv5 = 0.35;
global demastate5;
demastate5 = "";
global tbp5;
tbp5 = 1000000;
global tsp5;
tsp5 = 0;
global cc5;
cc5 = 0;

global tv6;
tv6 = 0.15;
global demastate6;
demastate6 = "";
global tbp6;
tbp6 = 1000000;
global tsp6;
tsp6 = 0;
global cc6;
cc6 = 0;

global tv7;
tv7 = 0.1;
global demastate7;
demastate7 = "";
global tbp7;
tbp7 = 1000000;
global tsp7;
tsp7 = 0;
global cc7;
cc7 = 0;

global tv8;
tv8 = 10;
global demastate8;
demastate8 = "";
global tbp8;
tbp8 = 1000000;
global tsp8;
tsp8 = 0;
global cc8;
cc8 = 0;

global tv9;
tv9 = 0.15;
global demastate9;
demastate9 = "";
global tbp9;
tbp9 = 1000000;
global tsp9;
tsp9 = 0;
global cc9;
cc9 = 0;

global tv10;
tv10 = 0.0002;
global demastate10;
demastate10 = "";
global tbp10;
tbp10 = 1000000;
global tsp10;
tsp10 = 0;
global cc10;
cc10 = 0;

print("Reconstructing DNN Models...");
# cgldModel = tf.keras.models.load_model("dnnCGLDModel.h5");
# print("Loaded CGLD DNN model!");
#
# forthModel = tf.keras.models.load_model("dnnFORTHModel.h5");
# print("Loaded FORTH DNN model!");
#
# lrcModel = tf.keras.models.load_model("dnnLRCModel.h5");
# print("Loaded LRC DNN model!");
#
# nmrModel = tf.keras.models.load_model("dnnNMRModel.h5");
# print("Loaded NMR DNN model!");
#
# umaModel = tf.keras.models.load_model("dnnUMAModel.h5");
# print("Loaded UMA DNN model!");
#
# balModel = tf.keras.models.load_model("dnnBALModel.h5");
# print("Loaded BAL DNN model!");
#
# filModel = tf.keras.models.load_model("dnnFILModel.h5");
# print("Loaded FIL DNN model!");
#
# renModel = tf.keras.models.load_model("dnnRENModel.h5");
# print("Loaded REN DNN model!");
#
# uniModel = tf.keras.models.load_model("dnnUNIModel.h5");
# print("Loaded UNI DNN model!");
#
# yfiModel = tf.keras.models.load_model("dnnYFIModel.h5");
# print("Loaded YFI DNN model!");
print("DONE\n");

global OKCYAN;
OKCYAN = '\033[96m';
global OKGREEN;
OKGREEN = '\033[92m';
global FAIL;
FAIL = '\033[91m';

logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',datefmt='%Y-%m-%d:%H:%M:%S',level=logging.ERROR);
logger = logging.getLogger(__name__);

while True:
    st = time.time();
    os.system('cls');
    # try:
    #     output = cc_cycle("CGLD-USD",tv1,demastate1,tbp1,tsp1,cc1);
    #     output = str(output).split(",");
    #     demastate1 = output[0];
    #     tbp1 = output[1];
    #     tsp1 = output[2];
    #     cc1 = output[3];
    #     time.sleep(1 - ((time.time() - st) % 1));
    # except Exception as e:
    #     logging.error('Caught exception: ' + str(e));
    #
    # try:
    #     output = cc_cycle("FORTH-USD",tv2,demastate2,tbp2,tsp2,cc2);
    #     output = str(output).split(",");
    #     demastate2 = output[0];
    #     tbp2 = output[1];
    #     tsp2 = output[2];
    #     cc2 = output[3];
    #     time.sleep(1 - ((time.time() - st) % 1));
    # except Exception as e:
    #     logging.error('Caught exception: ' + str(e));
    #
    # try:
    #     output = cc_cycle("LRC-USD",tv3,demastate3,tbp3,tsp3,cc3);
    #     output = str(output).split(",");
    #     demastate3 = output[0];
    #     tbp3 = output[1];
    #     tsp3 = output[2];
    #     cc3 = output[3];
    #     time.sleep(1 - ((time.time() - st) % 1));
    # except Exception as e:
    #     logging.error('Caught exception: ' + str(e));
    #
    # try:
    #     output = cc_cycle("NMR-USD",tv4,demastate4,tbp4,tsp4,cc4);
    #     output = str(output).split(",");
    #     demastate4 = output[0];
    #     tbp4 = output[1];
    #     tsp4 = output[2];
    #     cc4 = output[3];
    #     time.sleep(1 - ((time.time() - st) % 1));
    # except Exception as e:
    #     logging.error('Caught exception: ' + str(e));
    #
    # try:
    #     output = cc_cycle("UMA-USD",tv5,demastate5,tbp5,tsp5,cc5);
    #     output = str(output).split(",");
    #     demastate5 = output[0];
    #     tbp5 = output[1];
    #     tsp5 = output[2];
    #     cc5 = output[3];
    #     time.sleep(1 - ((time.time() - st) % 1));
    # except Exception as e:
    #     logging.error('Caught exception: ' + str(e));
    #
    # try:
    #     output = cc_cycle("BAL-USD",tv6,demastate6,tbp6,tsp6,cc6);
    #     output = str(output).split(",");
    #     demastate6 = output[0];
    #     tbp6 = output[1];
    #     tsp6 = output[2];
    #     cc6 = output[3];
    #     time.sleep(1 - ((time.time() - st) % 1));
    # except Exception as e:
    #     logging.error('Caught exception: ' + str(e));
    #
    # try:
    #     output = cc_cycle("FIL-USD",tv7,demastate7,tbp7,tsp7,cc7);
    #     output = str(output).split(",");
    #     demastate7 = output[0];
    #     tbp7 = output[1];
    #     tsp7 = output[2];
    #     cc7 = output[3];
    #     time.sleep(1 - ((time.time() - st) % 1));
    # except Exception as e:
    #     logging.error('Caught exception: ' + str(e));
    #
    # try:
    #     output = cc_cycle("REN-USD",tv8,demastate8,tbp8,tsp8,cc8);
    #     output = str(output).split(",");
    #     demastate8 = output[0];
    #     tbp8 = output[1];
    #     tsp8 = output[2];
    #     cc8 = output[3];
    #     time.sleep(1 - ((time.time() - st) % 1));
    # except Exception as e:
    #     logging.error('Caught exception: ' + str(e));
    #
    # try:
    #     output = cc_cycle("UNI-USD",uniModel,tv9,demastate9,tbp9,tsp9,cc9);
    #     output = str(output).split(",");
    #     demastate9 = output[0];
    #     tbp9 = output[1];
    #     tsp9 = output[2];
    #     cc9 = output[3];
    #     time.sleep(1 - ((time.time() - st) % 1));
    # except Exception as e:
    #     logging.error('Caught exception: ' + str(e));
    #
    # try:
    #     output = cc_cycle("YFI-USD",yfiModel,tv10,demastate10,tbp10,tsp10,cc10);
    #     output = str(output).split(",");
    #     demastate10 = output[0];
    #     tbp10 = output[1];
    #     tsp10 = output[2];
    #     cc10 = output[3];
    #     time.sleep(1 - ((time.time() - st) % 1));
    # except Exception as e:
    #     logging.error('Caught exception: ' + str(e));

    #sleep core for increment_pace seconds
    time.sleep(increment_pace - ((time.time() - st) % increment_pace));
