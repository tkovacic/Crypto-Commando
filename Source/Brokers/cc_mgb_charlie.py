#TITLE: cc_mgb_charlie.py
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
tv1 = 0.3;
global demastate1;
demastate1 = "";
global tbp1;
tbp1 = 1000000;
global tsp1;
tsp1 = 0;
global cc1;
cc1 = 0;

global tv2;
tv2 = 0.05;
global demastate2;
demastate2 = "";
global tbp2;
tbp2 = 1000000;
global tsp2;
tsp2 = 0;
global cc2;
cc2 = 0;

global tv3;
tv3 = 5;
global demastate3;
demastate3 = "";
global tbp3;
tbp3 = 1000000;
global tsp3;
tsp3 = 0;
global cc3;
cc3 = 0;

global tv4;
tv4 = 10;
global demastate4;
demastate4 = "";
global tbp4;
tbp4 = 1000000;
global tsp4;
tsp4 = 0;
global cc4;
cc4 = 0;

global tv5;
tv5 = 2;
global demastate5;
demastate5 = "";
global tbp5;
tbp5 = 1000000;
global tsp5;
tsp5 = 0;
global cc5;
cc5 = 0;

global tv6;
tv6 = 0.005;
global demastate6;
demastate6 = "";
global tbp6;
tbp6 = 1000000;
global tsp6;
tsp6 = 0;
global cc6;
cc6 = 0;

global tv7;
tv7 = 45;
global demastate7;
demastate7 = "";
global tbp7;
tbp7 = 1000000;
global tsp7;
tsp7 = 0;
global cc7;
cc7 = 0;

global tv8;
tv8 = 5;
global demastate8;
demastate8 = "";
global tbp8;
tbp8 = 1000000;
global tsp8;
tsp8 = 0;
global cc8;
cc8 = 0;

global tv9;
tv9 = 2;
global demastate9;
demastate9 = "";
global tbp9;
tbp9 = 1000000;
global tsp9;
tsp9 = 0;
global cc9;
cc9 = 0;

global tv10;
tv10 = 20;
global demastate10;
demastate10 = "";
global tbp10;
tbp10 = 1000000;
global tsp10;
tsp10 = 0;
global cc10;
cc10 = 0;

print("Reconstructing DNN Models...");
# linkModel = tf.keras.models.load_model("dnnLINKModel.h5");
# print("Loaded LINK DNN model!");

ltcModel = tf.keras.models.load_model("dnnLTCModel.h5");
print("Loaded LTC DNN model!");
#
# manaModel = tf.keras.models.load_model("dnnMANAModel.h5");
# print("Loaded MANA DNN model!");
#
# maticModel = tf.keras.models.load_model("dnnMATICModel.h5");
# print("Loaded MATIC DNN model!");
#
# mirModel = tf.keras.models.load_model("dnnMIRModel.h5");
# print("Loaded MIR DNN model!");
#
# mkrModel = tf.keras.models.load_model("dnnMKRModel.h5");
# print("Loaded MKR DNN model!");
#
# nknModel = tf.keras.models.load_model("dnnNKNModel.h5");
# print("Loaded NKN DNN model!");
#
# ognModel = tf.keras.models.load_model("dnnOGNModel.h5");
# print("Loaded OGN DNN model!");
#
# omgModel = tf.keras.models.load_model("dnnOMGModel.h5");
# print("Loaded OMG DNN model!");
#
# oxtModel = tf.keras.models.load_model("dnnOXTModel.h5");
# print("Loaded OXT DNN model!");
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
    #     #Clear screen and output debug info
    #     output = cc_cycle("LINK-USD",tv1,demastate1,tbp1,tsp1,cc1);
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
    #     output = cc_cycle("LTC-USD",ltcModel,tv2,demastate2,tbp2,tsp2,cc2);
    #     output = str(output).split(",");
    #     demastate2 = output[0];
    #     tbp2 = output[1];
    #     tsp2 = output[2];
    #     cc2 = output[3];
    #     time.sleep(1 - ((time.time() - st) % 1));
    # except Exception as e:
    #     logging.error('Caught exception: ' + str(e));

    # try:
    #     output = cc_cycle("MANA-USD",tv3,demastate3,tbp3,tsp3,cc3);
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
    #     output = cc_cycle("MATIC-USD",tv4,demastate4,tbp4,tsp4,cc4);
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
    #     output = cc_cycle("MIR-USD",tv5,demastate5,tbp5,tsp5,cc5);
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
    #     output = cc_cycle("MKR-USD",tv6,demastate6,tbp6,tsp6,cc6);
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
    #     output = cc_cycle("NKN-USD",tv7,demastate7,tbp7,tsp7,cc7);
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
    #     output = cc_cycle("OGN-USD",tv8,demastate8,tbp8,tsp8,cc8);
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
    #     output = cc_cycle("OMG-USD",tv9,demastate9,tbp9,tsp9,cc9);
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
    #     output = cc_cycle("OXT-USD",tv10,demastate10,tbp10,tsp10,cc10);
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
