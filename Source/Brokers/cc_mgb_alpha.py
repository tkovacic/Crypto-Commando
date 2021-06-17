#TITLE: cc_mgb_alpha.py
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
tv1 = 3;
global demastate1;
demastate1 = "";
global tbp1;
tbp1 = 1000000;
global tsp1;
tsp1 = 0;
global cc1;
cc1 = 0;

global tv2;
tv2 = 0.04;
global demastate2;
demastate2 = "";
global tbp2;
tbp2 = 1000000;
global tsp2;
tsp2 = 0;
global cc2;
cc2 = 0;

global tv3;
tv3 = 6;
global demastate3;
demastate3 = "";
global tbp3;
tbp3 = 1000000;
global tsp3;
tsp3 = 0;
global cc3;
cc3 = 0;

global tv4;
tv4 = 8;
global demastate4;
demastate4 = "";
global tbp4;
tbp4 = 1000000;
global tsp4
tsp4 = 0;
global cc4;
cc4 = 0;

global tv5;
tv5 = 10;
global demastate5;
demastate5 = "";
global tbp5;
tbp5 = 1000000;
global tsp5;
tsp5 = 0;
global cc5;
cc5 = 0;

global tv6;
tv6 = 0.0001;
global demastate6;
demastate6 = "";
global tbp6;
tbp6 = 1000000;
global tsp6;
tsp6 = 0;
global cc6;
cc6 = 0;

global tv7;
tv7 = 0.02;
global demastate7;
demastate7 = "";
global tbp7;
tbp7 = 1000000;
global tsp7;
tsp7 = 0;
global cc7;
cc7 = 0;

global tv8;
tv8 = 0.02;
global demastate8;
demastate8 = "";
global tbp8;
tbp8 = 1000000;
global tsp8;
tsp8 = 0;
global cc8;
cc8 = 0;

global tv9;
tv9 = 10;
global demastate9;
demastate9 = "";
global tbp9;
tbp9 = 1000000;
global tsp9;
tsp9 = 0;
global cc9;
cc9 = 0;

global tv10;
tv10 = 2;
global demastate10;
demastate10 = "";
global tbp10;
tbp10 = 1000000;
global tsp10;
tsp10 = 0;
global cc10;
cc10 = 0;

print("Reconstructing DNN Models...");
# inchModel = tf.keras.models.load_model("dnn1INCHModel.h5");
# print("Loaded 1INCH DNN model!");
#
# aaveModel = tf.keras.models.load_model("dnnAAVEModel.h5");
# print("Loaded AAVE DNN model!");
#
# adaModel = tf.keras.models.load_model("dnnADAModel.h5");
# print("Loaded ADA DNN model!");
#
# algoModel = tf.keras.models.load_model("dnnALGOModel.h5");
# print("Loaded ALGO DNN model!");
#
# ankrModel = tf.keras.models.load_model("dnnANKRModel.h5");
# print("Loaded ANKR DNN model!");
#
# btcModel = tf.keras.models.load_model("dnnBTCModel.h5");
# print("Loaded BTC DNN model!");
#
# compModel = tf.keras.models.load_model("dnnCOMPModel.h5");
# print("Loaded COMP DNN model!");
#
# dashModel = tf.keras.models.load_model("dnnDASHModel.h5");
# print("Loaded DASH DNN model!");
#
# enjModel = tf.keras.models.load_model("dnnENJModel.h5");
# print("Loaded ENJ DNN model!");
#
# eosModel = tf.keras.models.load_model("dnnEOSModel.h5");
# print("Loaded EOS DNN model!");
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
    #     os.system('cls');
    #     output = cc_cycle("1INCH-USD",inchModel,tv1,demastate1,tbp1,tsp1,cc1);
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
    #     output = cc_cycle("AAVE-USD",aaveModel,tv2,demastate2,tbp2,tsp2,cc2);
    #     output = str(output).split(",");
    #     demastate2 = output[0];
    #     tbp2 = output[1];
    #     tsp2 = output[2];
    #     cc2 = output[3];
    #     time.sleep(1 - ((time.time() - st) % 1));
    # except Exception as e:
    #     logging.error('Caught exception: ' + str(e));
    # try:
    #     output = cc_cycle("ADA-USD",adaModel,tv3,demastate3,tbp3,tsp3,cc3);
    #     output = str(output).split(",");
    #     demastate3 = output[0];
    #     tbp3 = output[1];
    #     tsp3 = output[2];
    #     cc3 = output[3];
    #     time.sleep(1 - ((time.time() - st) % 1));
    # except Exception as e:
    #     logging.error('Caught exception: ' + str(e));

    # try:
    #     output = cc_cycle("ALGO-USD",algoModel,tv4,demastate4,tbp4,tsp4,cc4);
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
    #     output = cc_cycle("ANKR-USD",ankrModel,tv5,demastate5,tbp5,tsp5,cc5);
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
    #     output = cc_cycle("BTC-USD",btcModel,tv6,demastate6,tbp6,tsp6,cc6);
    #     output = str(output).split(",");
    #     demastate6 = output[0];
    #     tbp6 = output[1];
    #     tsp6 = output[2];
    #     cc6 = output[3];
    #     time.sleep(1 - ((time.time() - st) % 1));
    # except Exception as e:
    #     logging.error('Caught exception: ' + str(e));

    # try:
    #     output = cc_cycle("COMP-USD",compModel,tv7,demastate7,tbp7,tsp7,cc7);
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
    #     output = cc_cycle("DASH-USD",dashModel,tv8,demastate8,tbp8,tsp8,cc8);
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
    #     output = cc_cycle("ENJ-USD",enjModel,tv9,demastate9,tbp9,tsp9,cc9);
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
    #     output = cc_cycle("EOS-USD",eosModel,tv10,demastate10,tbp10,tsp10,cc10);
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
